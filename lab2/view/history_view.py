import tkinter as tk
from tkinter import ttk


def history_view(root, history_data, go_back):
    """
    Экран просмотра истории.

    :param root: Основное окно Tkinter.
    :param history_data: Список истории (посещённого или созданного контента).
    :param go_back: Функция для возврата на предыдущий экран.
    """
    # Очистка текущего окна
    for widget in root.winfo_children():
        widget.destroy()

    # Заголовок
    tk.Label(root, text="History", font=("Arial", 16)).pack(pady=10)

    # Таблица с историей
    columns = ("#1", "#2", "#3")
    tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
    tree.pack(pady=10)

    tree.heading("#1", text="Content Name")
    tree.heading("#2", text="Date")
    tree.heading("#3", text="Rating")

    # Добавление данных в таблицу
    for record in history_data:
        tree.insert("", tk.END, values=(record["name"], record["date"], record["rating"]))

    # Кнопка возврата
    tk.Button(root, text="Back", width=20, command=go_back).pack(pady=10)


# Пример использования
if __name__ == "__main__":
    def mock_go_back():
        print("Going Back to Profile")

    example_history = [
        {"name": "Louvre Tour", "date": "2024-01-01", "rating": 5},
        {"name": "Eiffel Tower", "date": "2024-01-02", "rating": 4},
        {"name": "Notre Dame Cathedral", "date": "2024-01-03", "rating": 5},
    ]

    root = tk.Tk()
    root.title("History Screen")
    root.geometry("500x400")

    history_view(root, example_history, mock_go_back)

    root.mainloop()
