class UserController:
    def __init__(self, app):
        self.app = app
        self.user_service = app.services["user_service"]

    def control(self):
        profile_view = self.app.get_window("profile_view")
        history_view = self.app.get_window("history_view")
        edit_profile_view = self.app.get_window("edit_profile_view")

        profile_view.set_action("edit_profile", self.show_edit_profile)
        profile_view.set_action(
            "view_history",
            lambda: self.app.show_window("history_view")
            if self.app.current_user["status"] == "Tourist"
            else None,
        )
        profile_view.set_action("back", self.go_back)

        history_view.set_action("back", lambda: self.app.show_window("profile_view"))
        edit_profile_view.set_action("save", self.save_profile_changes)
        edit_profile_view.set_action("back", lambda: self.app.show_window("profile_view"))

    def show_edit_profile(self):
        edit_profile_view = self.app.get_window("edit_profile_view")
        user_data = self.app.current_user
        edit_profile_view.set_user_data(user_data)
        self.app.show_window("edit_profile_view")

    def save_profile_changes(self, updated_data):
        success = self.user_service.update_user(
            self.app.current_user["name"], updated_data
        )
        if success:
            print("Profile updated successfully!")
            self.app.current_user.update(updated_data)
            self.app.show_window("profile_view")
        else:
            print("Failed to update profile.")
            edit_profile_view = self.app.get_window("edit_profile_view")
            edit_profile_view.show_error("Failed to update profile. Try again.")

    def go_back(self):
        if self.app.current_user["status"] == "Tourist":
            self.app.show_window("tourist_main_view")
        elif self.app.current_user["status"] == "Guide":
            self.app.show_window("guide_main_view")
