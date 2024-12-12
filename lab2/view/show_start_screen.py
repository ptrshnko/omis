import tkinter as tk


def start_screen(root, go_to_login, go_to_register, exit_app):
    """
    Стартовая страница приложения.

    :param root: Основное окно Tkinter.
    :param go_to_login: Функция для перехода на страницу авторизации.
    :param go_to_register: Функция для перехода на страницу регистрации.
    :param exit_app: Функция для выхода из приложения.
    """
    # Очистка текущего окна
    for widget in root.winfo_children():
        widget.destroy()

    # Заголовок
    tk.Label(root, text="Virtual Tour and Travel Platform", font=("Arial", 16)).pack(pady=20)

    # Кнопки
    tk.Button(
        root,
        text="Log In",
        width=20,
        command=go_to_login,
    ).pack(pady=10)

    tk.Button(
        root,
        text="Register",
        width=20,
        command=go_to_register,
    ).pack(pady=10)

    tk.Button(
        root,
        text="Exit",
        width=20,
        command=exit_app,
    ).pack(pady=10)


# Пример использования
if __name__ == "__main__":
    def mock_go_to_login():
        print("Navigating to Login Screen!")

    def mock_go_to_register():
        print("Navigating to Register Screen!")

    def mock_exit_app():
        print("Exiting Application!")
        root.destroy()

    root = tk.Tk()
    root.title("Start Screen")
    root.geometry("400x300")

    start_screen(root, mock_go_to_login, mock_go_to_register, mock_exit_app)

    root.mainloop()
