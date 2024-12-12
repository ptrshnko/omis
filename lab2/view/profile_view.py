import tkinter as tk


def profile_view(root, user_data, edit_profile, view_history, go_back):
    """
    Экран профиля пользователя.

    :param root: Основное окно Tkinter.
    :param user_data: Данные пользователя (словарь с полями: "name", "status", "birth_year").
    :param edit_profile: Функция для редактирования профиля.
    :param view_history: Функция для просмотра истории (посещённого контента).
    :param go_back: Функция для возврата на главное окно.
    """
    # Очистка текущего окна
    for widget in root.winfo_children():
        widget.destroy()

    # Заголовок
    tk.Label(root, text="Profile", font=("Arial", 16)).pack(pady=10)

    # Информация о пользователе
    tk.Label(root, text=f"Full Name: {user_data['name']}").pack(pady=5)
    tk.Label(root, text=f"Status: {user_data['status']}").pack(pady=5)
    tk.Label(root, text=f"Birth Year: {user_data.get('birth_year', 'Unknown')}").pack(pady=5)
    # Кнопка редактирования профиля
    tk.Button(
        root,
        text="Edit Profile",
        width=20,
        command=edit_profile,
    ).pack(pady=10)

    # Кнопка просмотра истории только для туриста
    if user_data["status"] == "Tourist":
        tk.Button(
            root,
            text="View History",
            width=20,
            command=view_history,
        ).pack(pady=10)

    # Кнопка возврата
    tk.Button(
        root,
        text="Back",
        width=20,
        command=go_back,
    ).pack(pady=10)


# Пример использования
if __name__ == "__main__":
    def mock_edit_profile():
        print("Editing Profile")

    def mock_view_history():
        print("Viewing History")

    def mock_go_back():
        print("Going Back")

    user_tourist = {"name": "Alice", "status": "Tourist", "birth_year": 1995}
    user_guide = {"name": "Bob", "status": "Guide", "birth_year": 1985}

    root = tk.Tk()
    root.title("Profile Screen")
    root.geometry("400x300")

    # Для тестирования туриста
    print("Tourist Profile:")
    profile_view(root, user_tourist, mock_edit_profile, mock_view_history, mock_go_back)

    # Для тестирования гида (задержка перед обновлением для наглядности)
    root.after(3000, lambda: profile_view(root, user_guide, mock_edit_profile, mock_view_history, mock_go_back))

    root.mainloop()
