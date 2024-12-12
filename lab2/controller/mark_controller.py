class MarkController:
    def __init__(self, app):
        self.app = app
        self.mark_service = app.services["mark_service"]

    def control(self):
        history_view = self.app.get_window("history_view")
        history_view.set_action("create_mark", self.handle_create_mark)
        history_view.set_action("edit_mark", self.handle_edit_mark)
        history_view.set_action("delete_mark", self.handle_delete_mark)

    def handle_create_mark(self):
        create_view = self.app.get_window("create_experience_view")
        create_view.set_action("save", self.save_new_mark)
        create_view.set_action("cancel", lambda: self.app.show_window("history_view"))
        self.app.show_window("create_experience_view")

    def save_new_mark(self, mark_data):
        if self.mark_service.create_mark(mark_data):
            print("Mark created successfully.")
        else:
            print("Failed to create mark.")
        self.app.show_window("history_view")

    def handle_edit_mark(self, selected_mark):
        if not selected_mark:
            print("No mark selected.")
            return

        edit_view = self.app.get_window("experience_edit_view")
        edit_view.update_data(selected_mark)
        edit_view.set_action("save", self.save_edited_mark)
        edit_view.set_action("cancel", lambda: self.app.show_window("history_view"))
        self.app.show_window("experience_edit_view")

    def save_edited_mark(self, updated_data):
        if self.mark_service.update_mark(updated_data):
            print("Mark updated successfully.")
        else:
            print("Failed to update mark.")
        self.app.show_window("history_view")

    def handle_delete_mark(self, selected_mark):
        if not selected_mark:
            print("No mark selected.")
            return

        if self.mark_service.delete_mark(selected_mark):
            print(f"Mark {selected_mark['name']} deleted successfully.")
        else:
            print(f"Failed to delete mark {selected_mark['name']}.")
        self.app.show_window("history_view")


