import tkinter as tk
from tkinter import messagebox

def show_selection():
    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showwarning("Не выбрано", "Пожалуйста, выберите элемент из списка.")
        return
    selected_item = listbox.get(selected_indices[0])
    label_result.config(text=f"Вы выбрали: {selected_item}")

root = tk.Tk()
root.title("Listbox")
root.geometry("600x600+550+250")

label_info = tk.Label(root, text="Выберите элемент из списка:", font=("Arial", 12))
label_info.pack(pady=10)

frame_list = tk.Frame(root)
frame_list.pack(pady=5)

scrollbar = tk.Scrollbar(frame_list, orient=tk.VERTICAL)
listbox = tk.Listbox(frame_list, yscrollcommand=scrollbar.set, height=6, font=("Arial", 11))
scrollbar.config(command=listbox.yview)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

items = [
    "Python♥", "Java", "C++", "JavaScript", "C#", "Ruby", "Go", "Rust",
    "PHP", "Swift", "Kotlin", "TypeScript", "Scala", "Perl", "Haskell"
]
for item in items:
    listbox.insert(tk.END, item)

btn_select = tk.Button(root, text="Показать выбранное", command=show_selection, font=("Arial", 11))
btn_select.pack(pady=10)

label_result = tk.Label(root, text="Здесь будет ваш выбор", font=("Arial", 12, "bold"), fg="blue")
label_result.pack(pady=10)

root.mainloop()