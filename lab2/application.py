import tkinter as tk
from view.login_view import login_screen
from view.register_view import register_screen
from view.tourist_main_view import tourist_main_view
from view.guide_main_view import guide_main_view
from view.profile_view import profile_view
from view.history_view import history_view
from view.create_experience_view import create_experience_view
from view.content_viewer import content_viewer
from view.experience_edit_view import experience_edit_view
from view.show_start_screen import start_screen


class AppController:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Virtual Tour Platform")
        self.root.geometry("500x400")
        self.users = {}  # Словарь для хранения пользователей {имя: {пароль, статус}}
        self.user_data = None  # Данные текущего пользователя

    def run(self):
        self.show_login()
        self.root.mainloop()

    def show_login(self):
        login_screen(
            self.root,
            handle_login=self.handle_login,
            go_to_main_menu=self.show_start_screen
        )

    def show_register(self):
        register_screen(
            self.root,
            handle_register=self.handle_register,
            go_to_main_menu=self.show_start_screen
        )

    def handle_edit_profile(self):
        """
        Логика редактирования профиля.
        """
        print(f"Editing profile for user: {self.user_data['name']}")
        # Здесь можно перенаправить на экран редактирования профиля

    def show_profile(self):
        """
        Переход на экран профиля.
        """
        if not self.user_data:
            print("No user data available!")
            return

        go_back = self.show_tourist_main if self.user_data["status"] == "Tourist" else self.show_guide_main

        profile_view(
            self.root,
            user_data=self.user_data,
            edit_profile=self.show_edit_profile,
            view_history=self.show_history if self.user_data["status"] == "Tourist" else None,
            go_back=go_back
        )

    def show_history(self):
        history_data = self.get_history()
        history_view(self.root, history_data=history_data, go_back=self.show_profile)

    def show_create_experience(self):
        create_experience_view(
            self.root,
            handle_save=self.handle_save_experience,
            go_back=self.show_guide_main
        )

    def show_start_screen(self):
        start_screen(
            self.root,
            go_to_login=self.show_login,
            go_to_register=self.show_register,
            exit_app=self.root.quit,
        )

    def run(self):
        self.show_start_screen()
        self.root.mainloop()

    def show_content_viewer(self):
        slides = self.get_slides()
        content_viewer(self.root, slides=slides, go_back=self.show_tourist_main)

    def handle_register(self, name, password, birth_year, status):
        if name in self.users:
            print("User already exists!")
        else:
            self.users[name] = {"password": password, "status": status, "birth_year": birth_year}
            print(f"Registered {name} as {status}")
        self.show_login()

    def handle_login(self, name, password, status):
        """
        Обработка авторизации пользователя.

        :param name: Имя пользователя.
        :param password: Пароль пользователя.
        :param status: Статус пользователя (Tourist/Guide).
        """
        # Здесь пароль можно игнорировать, проверяем только статус
        if status == "Tourist":
            self.user_data = {"name": name, "status": "Tourist"}
            self.show_tourist_main()
        elif status == "Guide":
            self.user_data = {"name": name, "status": "Guide"}
            self.show_guide_main()
        else:
            print("Unknown status selected!")

    def show_tourist_main(self):
        tourist_main_view(
            self.root,
            view_profile=self.show_profile,  # Открывает профиль туриста
            apply_filters=self.apply_filters,
            start_viewing=lambda selected_item: self.show_experience_start_page(selected_item),
        )

    def show_guide_main(self):
        guide_main_view(
            self.root,
            edit_selected=self.show_experience_edit_page,
            delete_selected=self.handle_delete_experience,
            create_new=self.show_create_experience,
            go_to_profile=self.show_profile,  # Переход к профилю гида
        )

    def show_experience_edit_page(self, experience=None):
        """
        Переход на страницу редактирования контента.
        :param experience: Данные выбранного контента.
        """
        if experience:
            experience_edit_view(
                self.root,
                experience_data={
                    "name": experience[0],
                    "type": experience[1],
                    "country": experience[2],
                    "theme": experience[3],
                    "rating": experience[4],
                },
                handle_save=self.handle_save_experience_edit,
                go_back=self.show_guide_main
            )
        else:
            print("No experience selected!")

    def handle_save_experience_edit(self, updated_data):
        """
        Сохранение изменений для контента.
        :param updated_data: Обновленные данные контента.
        """
        print(f"Updated experience: {updated_data}")
        # Здесь можно добавить логику для сохранения в базу данных или обновления списка
        self.show_guide_main()

    def handle_edit_profile(self):
        # Здесь будет логика редактирования профиля
        print("Editing profile")

    def handle_save_experience(self, name, description, age, theme):
        # Здесь будет логика сохранения нового контента
        print(f"Saved Experience: {name}, {description}, {age}, {theme}")

    def show_edit_profile(self):
        """
        Переход на экран редактирования профиля.
        """

        def save_changes(name, birth_year):
            """
            Сохранение изменений профиля.
            """
            self.user_data["name"] = name
            self.user_data["birth_year"] = birth_year
            print(f"Profile updated: {self.user_data}")
            self.show_profile()

        from view.edit_profile_view import edit_profile_view
        edit_profile_view(
            self.root,
            user_data=self.user_data,
            save_changes=save_changes,
            go_back=self.show_profile
        )

    def handle_delete_experience(self, experience=None, table=None):
        if experience:
            print(f"Deleting experience: {experience}")
            # Логика удаления из таблицы
            for row in table.get_children():
                if table.item(row)["values"] == experience:
                    table.delete(row)
                    break
        else:
            print("No experience selected!")

    def apply_filters(self, *args):
        """
        Логика применения фильтров.
        """
        print(f"Filters applied: {args}")
        # Можно добавить обновление данных в таблице

    def get_history(self):
        # Заглушка для получения истории
        return [
            {"name": "Louvre Tour", "date": "2024-01-01", "rating": 5},
            {"name": "Eiffel Tower", "date": "2024-01-02", "rating": 4},
        ]

    def get_slides(self):
        # Заглушка для получения слайдов
        return [
            {"text": "Welcome to the Louvre Tour!", "image": "luvr.jpg", "video": "intro.mp4"},
            {"text": "The Mona Lisa is one of the most famous paintings in the world.", "image": "mona-lisa.jpg"},
            {"text": "The Venus de Milo is a celebrated ancient Greek statue.", "video": "venus.mp4"},
        ]

    def show_experience_start_page(self, experience=None):
        """
        Стартовая страница просмотра контента.
        """
        if experience:
            print(f"Starting experience: {experience}")
            self.show_content_viewer()
        else:
            print("No experience selected! Returning to main screen.")
            self.show_tourist_main()


# Запуск приложения
if __name__ == "__main__":
    app = AppController()
    app.run()
