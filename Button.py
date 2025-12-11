from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Кнопка")
root.geometry("600x600+550+250")
root.minsize(600, 600)

clicks = 0

def click():
    global clicks
    clicks += 1
    btn["text"] = f"Зачем ты нажал сюда {clicks} раз?"
    if clicks >= 10:
        btn["text"] = "Ну все хватит"
    print(btn["text"])

btn = ttk.Button(root, text="<Нажми сюда!>", command=click)
btn.place(relx=.5, rely=.5, anchor="c", relwidth=.4, relheight=.25  )
root.mainloop()

root.mainloop()
