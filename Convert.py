import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt5.QtCore import Qt

class SimpleCurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.rates = {
            'USD': 1.0,
            'EUR': 0.93,
            'RUB': 80.0,
            'GBP': 0.79,
            'JPY': 150.0
        }
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Конвертер валют')
        self.setFixedSize(350, 200)

        layout = QVBoxLayout()
        layout.setSpacing(10)

        title = QLabel('Конвертер валют')
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet('font-size: 16px; font-weight: bold;')
        layout.addWidget(title)

        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText('Введите сумму')
        self.amount_input.setText('100')
        layout.addWidget(self.amount_input)

        currency_layout = QHBoxLayout()

        self.from_combo = QComboBox()
        self.from_combo.addItems(['USD', 'EUR', 'RUB', 'GBP', 'JPY'])
        currency_layout.addWidget(self.from_combo)

        swap_btn = QPushButton('⇄')
        swap_btn.setFixedWidth(40)
        swap_btn.clicked.connect(self.swap_currencies)
        currency_layout.addWidget(swap_btn)

        self.to_combo = QComboBox()
        self.to_combo.addItems(['USD', 'EUR', 'RUB', 'GBP', 'JPY'])
        self.to_combo.setCurrentText('RUB')
        currency_layout.addWidget(self.to_combo)

        layout.addLayout(currency_layout)

        convert_btn = QPushButton('Конвертировать')
        convert_btn.clicked.connect(self.convert)
        layout.addWidget(convert_btn)

        self.result_label = QLabel('')
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet('font-size: 14px; color: blue;')
        layout.addWidget(self.result_label)

        self.rate_label = QLabel('')
        self.rate_label.setAlignment(Qt.AlignCenter)
        self.update_rate_label()
        layout.addWidget(self.rate_label)

        self.setLayout(layout)

    def update_rate_label(self):
        from_curr = self.from_combo.currentText()
        to_curr = self.to_combo.currentText()
        rate = self.rates[to_curr] / self.rates[from_curr]
        self.rate_label.setText(f'1 {from_curr} = {rate:.2f} {to_curr}')

    def swap_currencies(self):
        from_curr = self.from_combo.currentText()
        to_curr = self.to_combo.currentText()

        self.from_combo.setCurrentText(to_curr)
        self.to_combo.setCurrentText(from_curr)

        self.update_rate_label()
        self.convert()

    def convert(self):
        try:
            amount = float(self.amount_input.text())

            from_curr = self.from_combo.currentText()
            to_curr = self.to_combo.currentText()

            result = amount * (self.rates[to_curr] / self.rates[from_curr])

            self.result_label.setText(f'{amount:.2f} {from_curr} = {result:.2f} {to_curr}')

            self.update_rate_label()

        except ValueError:
            self.result_label.setText('Ошибка: введите число')
            self.result_label.setStyleSheet('color: red;')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = SimpleCurrencyConverter()
    converter.show()
    sys.exit(app.exec_())