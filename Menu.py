from tkinter import *

root = Tk()
root.title("Menu")
root.geometry("250x150")

root.option_add("*tearOff", FALSE)

main_menu = Menu()
file_menu = Menu()
settings_menu = Menu()

settings_menu.add_command(label="Save")
settings_menu.add_command(label="Open")

file_menu.add_cascade(label="Settings", menu=settings_menu)
file_menu.add_separator()
file_menu.add_command(label="Exit")

main_menu.add_cascade(label="File", menu=file_menu)

root.config(menu=main_menu)
root.mainloop()