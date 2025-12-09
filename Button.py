import tkinter as ttk
from fileinput import close

root = ttk.Tk()
root.title("Кнопка")
root.geometry("600x500+550+250")
root.minsize(600, 500)

clicks = 0

def click():
    global clicks
    clicks += 1
    btn["text"] = f"Зачем ты нажал сюда {clicks} раз?"
btn = ttk.Button(root, text="<Нажми сюда!>", command=click)
btn.pack()

root.mainloop()
