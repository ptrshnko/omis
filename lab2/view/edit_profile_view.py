import tkinter as tk


def edit_profile_view(root, user_data, save_changes, go_back):
    """
    Окно редактирования профиля пользователя.

    :param root: Основное окно Tkinter.
    :param user_data: Текущие данные пользователя.
    :param save_changes: Функция для сохранения изменений.
    :param go_back: Функция для возврата к профилю.
    """
    # Очистка текущего окна
    for widget in root.winfo_children():
        widget.destroy()

    # Заголовок
    tk.Label(root, text="Edit Profile", font=("Arial", 16)).pack(pady=10)

    # Поля для редактирования
    tk.Label(root, text="Full Name").pack(pady=5)
    name_entry = tk.Entry(root, width=30)
    name_entry.insert(0, user_data.get("name", ""))
    name_entry.pack(pady=5)

    tk.Label(root, text="Birth Year").pack(pady=5)
    birth_year_entry = tk.Entry(root, width=30)
    birth_year_entry.insert(0, user_data.get("birth_year", ""))
    birth_year_entry.pack(pady=5)

    # Кнопка сохранения изменений
    tk.Button(
        root,
        text="Save Changes",
        width=20,
        command=lambda: save_changes(
            name=name_entry.get(),
            birth_year=birth_year_entry.get()
        )
    ).pack(pady=10)

    # Кнопка возврата
    tk.Button(
        root,
        text="Back",
        width=20,
        command=go_back,
    ).pack(pady=10)

