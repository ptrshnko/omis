class SlideController:
    def __init__(self, app):
        self.app = app
        self.slide_service = app.services["slide_service"]

    def control(self):
        content_view = self.app.get_window("content_viewer")
        content_view.set_action("add_slide", self.handle_create_slide)
        content_view.set_action("edit_slide", self.handle_edit_slide)
        content_view.set_action("delete_slide", self.handle_delete_slide)

    def handle_create_slide(self):
        create_view = self.app.get_window("create_experience_view")
        create_view.set_action("save", self.save_new_slide)
        create_view.set_action("cancel", lambda: self.app.show_window("content_viewer"))
        self.app.show_window("create_experience_view")

    def save_new_slide(self, slide_data):
        if self.slide_service.create_slide(slide_data):
            print("Slide created successfully.")
        else:
            print("Failed to create slide.")
        self.app.show_window("content_viewer")

    def handle_edit_slide(self, selected_slide):
        if not selected_slide:
            print("No slide selected.")
            return

        edit_view = self.app.get_window("experience_edit_view")
        edit_view.update_data(selected_slide)
        edit_view.set_action("save", self.save_edited_slide)
        edit_view.set_action("cancel", lambda: self.app.show_window("content_viewer"))
        self.app.show_window("experience_edit_view")

    def save_edited_slide(self, updated_data):
        if self.slide_service.update_slide(updated_data):
            print("Slide updated successfully.")
        else:
            print("Failed to update slide.")
        self.app.show_window("content_viewer")

    def handle_delete_slide(self, selected_slide):
        if not selected_slide:
            print("No slide selected.")
            return

        if self.slide_service.delete_slide(selected_slide):
            print(f"Slide {selected_slide['text']} deleted successfully.")
        else:
            print(f"Failed to delete slide {selected_slide['text']}.")
        self.app.show_window("content_viewer")
