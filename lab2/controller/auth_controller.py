from view.login_view import login_screen
from view.register_view import register_screen
from view.show_start_screen import start_screen


class AuthController:

    def __init__(self, app):
        self.app = app

    def show_start_screen(self):
        start_screen(
            self.app.root,
            go_to_login=self.show_login,
            go_to_register=self.show_register,
            exit_app=self.app.root.quit,
        )

    def show_login(self):
        login_screen(
            self.app.root,
            handle_login=self.handle_login,
            go_to_main_menu=self.app.show_start_screen
        )

    def show_register(self):
        register_screen(
            self.app.root,
            handle_register=self.handle_register,
            go_to_main_menu=self.app.show_start_screen
        )

    def handle_register(self, name, password, birth_year, status):
        if name in self.app.users:
            print("User already exists!")
        else:
            self.app.users[name] = {"password": password, "status": status, "birth_year": birth_year}
            print(f"Registered {name} as {status}")
        self.show_login()

    def handle_login(self, name, password, status):
        if status == "Tourist":
            self.app.user_data = {"name": name, "status": "Tourist"}
            self.app.show_tourist_main()
        elif status == "Guide":
            self.app.user_data = {"name": name, "status": "Guide"}
            self.app.show_guide_main()
        else:
            print("Unknown status selected!")
