import tkinter as tk


def experience_edit_view(root, experience_data, handle_save, go_back):
    """
    Экран редактирования контента.

    :param root: Основное окно Tkinter.
    :param experience_data: Данные выбранного контента для редактирования.
    :param handle_save: Функция для сохранения изменений.
    :param go_back: Функция для возврата на предыдущий экран.
    """
    # Очистка текущего окна
    for widget in root.winfo_children():
        widget.destroy()

    # Заголовок
    tk.Label(root, text="Edit Content", font=("Arial", 16)).pack(pady=10)

    # Поля для редактирования
    tk.Label(root, text="Name").pack()
    name_entry = tk.Entry(root, width=30)
    name_entry.insert(0, experience_data["name"])
    name_entry.pack()

    tk.Label(root, text="Type").pack()
    type_entry = tk.Entry(root, width=30)
    type_entry.insert(0, experience_data["type"])
    type_entry.pack()

    tk.Label(root, text="Country").pack()
    country_entry = tk.Entry(root, width=30)
    country_entry.insert(0, experience_data["country"])
    country_entry.pack()

    tk.Label(root, text="Theme").pack()
    theme_entry = tk.Entry(root, width=30)
    theme_entry.insert(0, experience_data["theme"])
    theme_entry.pack()

    tk.Label(root, text="Rating").pack()
    rating_entry = tk.Entry(root, width=30)
    rating_entry.insert(0, str(experience_data["rating"]))
    rating_entry.pack()

    # Кнопки
    tk.Button(
        root,
        text="Save Changes",
        command=lambda: handle_save({
            "name": name_entry.get(),
            "type": type_entry.get(),
            "country": country_entry.get(),
            "theme": theme_entry.get(),
            "rating": rating_entry.get()
        }),
        width=20
    ).pack(pady=10)

    tk.Button(root, text="Back", command=go_back, width=20).pack(pady=10)


# Пример использования
if __name__ == "__main__":
    def mock_handle_save(updated_data):
        print(f"Saved changes: {updated_data}")

    def mock_go_back():
        print("Returning to previous screen")

    root = tk.Tk()
    root.title("Edit Experience")
    root.geometry("400x500")

    example_data = {
        "name": "Eiffel Tower Tour",
        "type": "Excursion",
        "country": "France",
        "theme": "Architecture",
        "rating": 9.0
    }

    experience_edit_view(
        root,
        experience_data=example_data,
        handle_save=mock_handle_save,
        go_back=mock_go_back
    )

    root.mainloop()
