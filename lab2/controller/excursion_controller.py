class ExcursionController:

    def __init__(self, app):

        self.app = app
        self.excursion_service = app.services["excursion_service"]

    def control(self):

        guide_main_view = self.app.get_window("guide_main_view")
        create_experience_view = self.app.get_window("create_experience_view")
        experience_edit_view = self.app.get_window("experience_edit_view")

        guide_main_view.set_action("create_new", self.show_create_experience)
        guide_main_view.set_action("edit_selected", self.show_edit_experience)
        guide_main_view.set_action("delete_selected", self.delete_experience)

        create_experience_view.set_action("save", self.save_new_experience)
        create_experience_view.set_action("back", lambda: self.app.show_window("guide_main_view"))

        experience_edit_view.set_action("save", self.save_edited_experience)
        experience_edit_view.set_action("back", lambda: self.app.show_window("guide_main_view"))

    def show_create_experience(self):

        create_experience_view = self.app.get_window("create_experience_view")
        create_experience_view.clear_fields()
        self.app.show_window("create_experience_view")

    def save_new_experience(self, experience_data):

        success = self.excursion_service.add_experience(experience_data)
        if success:
            print("Experience created successfully!")
            self.app.show_window("guide_main_view")
        else:
            print("Failed to create experience.")
            create_experience_view = self.app.get_window("create_experience_view")
            create_experience_view.show_error("Failed to create experience. Try again.")

    def show_edit_experience(self, selected_experience):

        if selected_experience:
            experience_edit_view = self.app.get_window("experience_edit_view")
            experience_edit_view.set_experience_data(selected_experience)
            self.app.show_window("experience_edit_view")
        else:
            print("No experience selected!")

    def save_edited_experience(self, updated_data):

        success = self.excursion_service.update_experience(updated_data)
        if success:
            print("Experience updated successfully!")
            self.app.show_window("guide_main_view")
        else:
            print("Failed to update experience.")
            experience_edit_view = self.app.get_window("experience_edit_view")
            experience_edit_view.show_error("Failed to update experience. Try again.")

    def delete_experience(self, selected_experience):

        if selected_experience:
            success = self.excursion_service.delete_experience(selected_experience)
            if success:
                print("Experience deleted successfully!")
                guide_main_view = self.app.get_window("guide_main_view")
                guide_main_view.refresh_table()
            else:
                print("Failed to delete experience.")
        else:
            print("No experience selected!")
