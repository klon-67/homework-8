import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Вибір мови")
window.geometry("350x250")

language = tk.StringVar(value="Python")

label = tk.Label(window, text="Оберіть мову програмування:")
label.pack(pady=10)


def show_language():
    messagebox.showinfo("Вибрана мова", f"Ви обрали: {language.get()}")

tk.Radiobutton(window, text="Python", variable=language,
               value="Python", command=show_language).pack()

tk.Radiobutton(window, text="Java", variable=language,
               value="Java", command=show_language).pack()

tk.Radiobutton(window, text="C++", variable=language,
               value="C++", command=show_language).pack()

window.mainloop()
