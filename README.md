# Завдання 3 — Вибір мови програмування

## Опис програми

Ця програма на Python створює графічне вікно за допомогою бібліотеки `tkinter`.

У вікні розміщено три радіо-кнопки для вибору мови програмування:

* Python
* Java
* C++

Після натискання на одну з кнопок з'являється повідомлення з вибраною мовою.

## Код

```python
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

tk.Radiobutton(
    window, text="Python",
    variable=language,
    value="Python",
    command=show_language
).pack()

tk.Radiobutton(
    window, text="Java",
    variable=language,
    value="Java",
    command=show_language
).pack()

tk.Radiobutton(
    window, text="C++",
    variable=language,
    value="C++",
    command=show_language
).pack()

window.mainloop()
```

## Запуск

Для запуску програми потрібно мати встановлений **Python 3**.

Запустіть файл командою:

```bash
python main.py
```

## Результат

Після запуску відкриється вікно з трьома радіо-кнопками. При виборі мови з'явиться повідомлення:

**«Ви обрали: Python»**

або назва іншої вибраної мови.

## Використані бібліотеки

* `tkinter` — для створення графічного інтерфейсу.
* `messagebox` — для виведення повідомлення.

## Автор

Учень/учениця
