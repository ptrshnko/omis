import tkinter as tk
from tkinter import ttk


def tourist_main_view(root, view_profile, apply_filters, start_viewing):
    """
    Главное окно туриста с таблицей популярных экскурсий, фильтрами и функционалом для просмотра.

    :param root: Основное окно Tkinter.
    :param view_profile: Функция для перехода в профиль.
    :param apply_filters: Функция для применения фильтров и обновления таблицы.
    :param start_viewing: Функция для начала просмотра выбранной достопримечательности.
    """
    # Очистка окна
    for widget in root.winfo_children():
        widget.destroy()

    # Заголовок
    tk.Label(root, text="Welcome, Tourist!", font=("Arial", 16)).pack(pady=10)

    # Поле поиска
    search_frame = tk.Frame(root)
    search_frame.pack(pady=5)

    tk.Label(search_frame, text="Search by name:").grid(row=0, column=0, padx=5)
    search_entry = tk.Entry(search_frame, width=20)
    search_entry.grid(row=0, column=1, padx=5)

    tk.Button(search_frame, text="Search", command=lambda: apply_filters(search_entry.get())).grid(row=0, column=2, padx=5)

    # Фильтры
    filters_frame = tk.Frame(root)
    filters_frame.pack(pady=5)

    tk.Label(filters_frame, text="Country/City:").grid(row=0, column=0, padx=5)
    country_filter = ttk.Combobox(filters_frame, values=["All", "France", "USA", "Japan"], width=10)
    country_filter.grid(row=0, column=1, padx=5)

    tk.Label(filters_frame, text="Theme:").grid(row=0, column=2, padx=5)
    theme_filter = ttk.Combobox(filters_frame, values=["All", "History", "Food", "Architecture"], width=10)
    theme_filter.grid(row=0, column=3, padx=5)

    tk.Label(filters_frame, text="Type:").grid(row=0, column=4, padx=5)
    type_filter = ttk.Combobox(filters_frame, values=["All", "Excursion", "Travel"], width=10)
    type_filter.grid(row=0, column=5, padx=5)

    tk.Button(filters_frame, text="Apply Filters", command=lambda: apply_filters(
        search_entry.get(),
        country_filter.get(),
        theme_filter.get(),
        type_filter.get()
    )).grid(row=0, column=6, padx=5)

    # Таблица популярных экскурсий
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
        ("Eiffel Tower Tour", "Excursion", "France", "Architecture", 9.0),
        ("New York City Highlights", "Travel", "USA", "History", 8.5),
        ("Tokyo Food Journey", "Travel", "Japan", "Food", 9.2),
        ("Versailles Palace Tour", "Excursion", "France", "History", 8.8),
    ]
    for item in example_data:
        table.insert("", tk.END, values=item)

    # Кнопка перехода к профилю
    tk.Button(root, text="Go to Profile", width=20, command=view_profile).pack(pady=5)

    # Кнопка начала просмотра
    tk.Button(
        root,
        text="Start Viewing",
        width=20,
        command=lambda: start_viewing(table.item(table.selection())["values"] if table.selection() else None)
    ).pack(pady=5)


# Пример использования
if __name__ == "__main__":
    def mock_view_profile():
        print("Navigating to Profile")

    def mock_apply_filters(*args):
        print(f"Applying Filters: {args}")

    def mock_start_viewing(selected_item):
        if selected_item:
            print(f"Starting viewing for: {selected_item}")
        else:
            print("No item selected!")

    root = tk.Tk()
    root.title("Tourist Main Window")
    root.geometry("700x500")

    tourist_main_view(root, mock_view_profile, mock_apply_filters, mock_start_viewing)

    root.mainloop()
