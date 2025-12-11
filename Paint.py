import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLabel, QButtonGroup,
                             QToolButton, QFileDialog)
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap, QPolygon


class DrawingCanvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(800, 600)
        self.image = QPixmap(800, 600)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brush_color = QColor(0, 0, 0)
        self.brush_size = 2
        self.tool = "pencil"
        self.start_point = QPoint()
        self.end_point = QPoint()
        self.last_point = QPoint()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image, self.image.rect())

        if self.drawing and self.tool != "pencil":
            painter.setPen(QPen(self.brush_color, self.brush_size))
            self.draw_shape(painter, self.start_point, self.end_point)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.start_point = self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self.drawing:
            if self.tool == "pencil":
                painter = QPainter(self.image)
                painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine,
                                    Qt.RoundCap, Qt.RoundJoin))
                painter.drawLine(self.last_point, event.pos())
                self.last_point = event.pos()
                self.update()
            else:
                self.end_point = event.pos()
                self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.drawing:
            self.end_point = event.pos()
            if self.tool != "pencil":
                painter = QPainter(self.image)
                painter.setPen(QPen(self.brush_color, self.brush_size))
                self.draw_shape(painter, self.start_point, self.end_point)
                self.update()
            self.drawing = False

    def draw_shape(self, painter, start, end):
        x1, y1 = start.x(), start.y()
        x2, y2 = end.x(), end.y()
        rect = QRect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))

        if self.tool == "line":
            painter.drawLine(start, end)
        elif self.tool == "rectangle":
            painter.drawRect(rect)
        elif self.tool == "circle":
            painter.drawEllipse(rect)
        elif self.tool == "triangle":
            top = QPoint(x1, y1)
            bottom_right = QPoint(x2, y2)
            bottom_left = QPoint(x1, y2)
            triangle = QPolygon([top, bottom_right, bottom_left])
            painter.drawPolygon(triangle)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def save_image(self, filename):
        self.image.save(filename)

    def set_tool(self, tool):
        self.tool = tool


class DrawingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Рисование фигур мышью")
        self.setGeometry(100, 100, 1000, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        self.canvas = DrawingCanvas()

        tool_panel = QWidget()
        tool_panel.setFixedWidth(180)
        tool_layout = QVBoxLayout(tool_panel)

        tool_layout.addWidget(QLabel("Инструменты"))

        self.tool_group = QButtonGroup()
        tools = [("pencil", "Карандаш"), ("line", "Линия"),
                 ("rectangle", "Прямоугольник"), ("circle", "Круг"),
                 ("triangle", "Треугольник")]

        for tool, name in tools:
            btn = QToolButton()
            btn.setText(name)
            btn.setCheckable(True)
            self.tool_group.addButton(btn)
            tool_layout.addWidget(btn)
            btn.clicked.connect(lambda checked, t=tool: self.canvas.set_tool(t))

        self.tool_group.buttons()[0].setChecked(True)
        tool_layout.addStretch()

        clear_btn = QPushButton("Очистить")
        clear_btn.clicked.connect(self.canvas.clear)
        tool_layout.addWidget(clear_btn)

        save_btn = QPushButton("Сохранить")
        save_btn.clicked.connect(self.save_file)
        tool_layout.addWidget(save_btn)

        main_layout.addWidget(tool_panel)
        main_layout.addWidget(self.canvas, stretch=1)

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(
            self, "Сохранить", "", "PNG (*.png);;JPEG (*.jpg)")
        if filename:
            self.canvas.save_image(filename)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrawingApp()
    window.show()
    sys.exit(app.exec_())