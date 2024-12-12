class AuthController:

    def __init__(self, app):

        self.app = app
        self.auth_service = app.services["auth_service"]

    def control(self):

        login_view = self.app.get_window("login_view")
        register_view = self.app.get_window("register_view")

        login_view.set_action("login", self.handle_login)
        login_view.set_action("back", lambda: self.app.show_window("start_screen"))

        register_view.set_action("register", self.handle_register)
        register_view.set_action("back", lambda: self.app.show_window("start_screen"))

    def handle_login(self, login_data):

        username, password, status = login_data["username"], login_data["password"], login_data["status"]

        if self.auth_service.login(username, password, status):
            print(f"Login successful: {username} as {status}")
            self.app.current_user = self.auth_service.get_current_user()
            if status == "Tourist":
                self.app.show_window("tourist_main_view")
            elif status == "Guide":
                self.app.show_window("guide_main_view")
        else:
            print("Login failed! Invalid credentials or status mismatch.")
            login_view = self.app.get_window("login_view")
            login_view.show_error("Invalid username, password, or status.")

    def handle_register(self, register_data):

        username, password, birth_year, status = (
            register_data["username"],
            register_data["password"],
            register_data["birth_year"],
            register_data["status"],
        )

        if self.auth_service.register(username, password, birth_year, status):
            print(f"Registration successful: {username} as {status}")
            self.app.show_window("login_view")
        else:
            print("Registration failed! User may already exist.")
            register_view = self.app.get_window("register_view")
            register_view.show_error("Registration failed. User already exists.")
