from view.history_view import history_view
from view.profile_view import profile_view


class UserController:
    def __init__(self, app):
        self.app = app

    def handle_edit_profile(self):
        print(f"Editing profile for user: {self.app.user_data['name']}")

    def show_profile(self):
        if not self.app.user_data:
            print("No user data available!")
            return

        go_back = self.app.show_tourist_main if self.app.user_data["status"] == "Tourist" else self.app.show_guide_main

        profile_view(
            self.app.root,
            user_data=self.app.user_data,
            edit_profile=self.app.show_edit_profile,
            view_history=self.app.show_history if self.app.user_data["status"] == "Tourist" else None,
            go_back=go_back
        )

    def show_edit_profile(self):
        def save_changes(name, birth_year):
            self.app.user_data["name"] = name
            self.app.user_data["birth_year"] = birth_year
            print(f"Profile updated: {self.app.user_data}")
            self.show_profile()

        from view.edit_profile_view import edit_profile_view
        edit_profile_view(
            self.app.root,
            user_data=self.app.user_data,
            save_changes=save_changes,
            go_back=self.show_profile
        )

    def show_history(self):
        history_data = self.app.get_history()
        history_view(self.app.root, history_data=history_data, go_back=self.show_profile)


    @staticmethod
    def get_history():
        return [
            {"name": "Louvre Tour", "date": "2024-01-01", "rating": 5},
            {"name": "Eiffel Tower", "date": "2024-01-02", "rating": 4},
        ]
