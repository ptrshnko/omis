import tkinter as tk
from tkinter import ttk


def login_screen(root, handle_login, go_to_main_menu):
    """
    Экран авторизации с выбором статуса.

    :param root: Основное окно Tkinter.
    :param handle_login: Функция для обработки логина.
    :param go_to_main_menu: Функция для возврата в главное меню.
    """
    # Очистка текущего окна
    for widget in root.winfo_children():
        widget.destroy()

    # Заголовок
    tk.Label(root, text="Log In", font=("Arial", 14)).pack(pady=10)

    # Поле ввода полного имени
    tk.Label(root, text="Full Name").pack()
    full_name_entry = tk.Entry(root, width=30)
    full_name_entry.pack()

    # Поле ввода пароля
    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*", width=30)
    password_entry.pack()

    # Выбор статуса (Tourist/Guide)
    tk.Label(root, text="Status").pack()
    status_combobox = ttk.Combobox(root, values=["Tourist", "Guide"], state="readonly", width=28)
    status_combobox.pack()
    status_combobox.current(0)  # По умолчанию "Tourist"

    # Кнопки
    tk.Button(
        root,
        text="Log In",
        width=20,
        command=lambda: handle_login(
            full_name_entry.get(),
            password_entry.get(),
            status_combobox.get(),
        ),
    ).pack(pady=10)

    tk.Button(root, text="Back", width=20, command=go_to_main_menu).pack(pady=10)


