import tkinter as tk


def create_experience_view(root, handle_save, go_back):
    """
    Экран создания нового контента.

    :param root: Основное окно Tkinter.
    :param handle_save: Функция для сохранения нового контента.
    :param go_back: Функция для возврата на главное окно гида.
    """
    # Очистка текущего окна
    for widget in root.winfo_children():
        widget.destroy()

    # Заголовок
    tk.Label(root, text="Create New Experience", font=("Arial", 16)).pack(pady=10)

    # Поля ввода
    tk.Label(root, text="Name").pack(pady=5)
    name_entry = tk.Entry(root, width=40)
    name_entry.pack()

    tk.Label(root, text="Description").pack(pady=5)
    description_text = tk.Text(root, width=40, height=5)
    description_text.pack()

    tk.Label(root, text="Age Restriction").pack(pady=5)
    age_entry = tk.Entry(root, width=40)
    age_entry.pack()

    tk.Label(root, text="Theme").pack(pady=5)
    theme_entry = tk.Entry(root, width=40)
    theme_entry.pack()

    # Кнопки
    tk.Button(
        root,
        text="Save",
        width=20,
        command=lambda: handle_save(
            name_entry.get(),
            description_text.get("1.0", tk.END).strip(),
            age_entry.get(),
            theme_entry.get(),
        ),
    ).pack(pady=10)

    tk.Button(root, text="Back", width=20, command=go_back).pack(pady=10)


