import tkinter as tk
from tkinter import ttk


def guide_main_view(root, edit_selected, delete_selected, create_new, go_to_profile):
    """
    Главное окно гида с таблицей его контента.

    :param root: Основное окно Tkinter.
    :param edit_selected: Функция для редактирования выбранного контента.
    :param delete_selected: Функция для удаления выбранного контента.
    :param create_new: Функция для создания нового контента.
    :param go_to_profile: Функция для перехода в профиль.
    """
    # Очистка текущего окна
    for widget in root.winfo_children():
        widget.destroy()

    # Заголовок
    tk.Label(root, text="Guide Dashboard", font=("Arial", 16)).pack(pady=10)

    # Таблица контента
    table_frame = tk.Frame(root)
    table_frame.pack(pady=10)

    columns = ("Name", "Type", "Country", "Theme", "Rating")
    table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
    table.pack()

    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=100)

    # Добавление примерных данных
    example_data = [
        ("Louvre Tour", "Excursion", "France", "History", 4.5),
        ("NYC Walk", "Travel", "USA", "Culture", 4.0),
        ("Tokyo Food", "Excursion", "Japan", "Food", 4.8),
    ]
    for item in example_data:
        table.insert("", tk.END, values=item)

    # Кнопки
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    tk.Button(
        button_frame,
        text="Edit Selected",
        command=lambda: edit_selected(table.item(table.focus())["values"] if table.focus() else None),
        width=20,
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        button_frame,
        text="Delete Selected",
        command=lambda: delete_selected(
            table.item(table.focus())["values"] if table.focus() else None,
            table,
        ),
        width=20,
    ).grid(row=0, column=1, padx=5)

    tk.Button(
        button_frame,
        text="Create New",
        command=create_new,
        width=20,
    ).grid(row=0, column=2, padx=5)

    tk.Button(
        button_frame,
        text="Go to Profile",
        command=go_to_profile,
        width=20,
    ).grid(row=0, column=3, padx=5)


# Пример использования
if __name__ == "__main__":
    def mock_edit_selected(item):
        if item:
            print(f"Editing item: {item}")
        else:
            print("No item selected!")

    def mock_delete_selected(item, table):
        if item:
            print(f"Deleting item: {item}")
            for row in table.get_children():
                if table.item(row)["values"] == item:
                    table.delete(row)
                    break
        else:
            print("No item selected!")

    def mock_create_new():
        print("Creating new content!")

    def mock_go_to_profile():
        print("Navigating to Profile!")

    root = tk.Tk()
    root.title("Guide Main View")
    root.geometry("700x500")

    guide_main_view(
        root,
        edit_selected=mock_edit_selected,
        delete_selected=mock_delete_selected,
        create_new=mock_create_new,
        go_to_profile=mock_go_to_profile,
    )

    root.mainloop()
