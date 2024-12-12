class TravelController:
    def __init__(self, app):
        self.app = app
        self.travel_service = app.services["travel_service"]

    def control(self):
        guide_main_view = self.app.get_window("guide_main_view")
        create_experience_view = self.app.get_window("create_experience_view")
        experience_edit_view = self.app.get_window("experience_edit_view")

        guide_main_view.set_action("create_new_travel", self.show_create_travel)
        guide_main_view.set_action("edit_selected_travel", self.show_edit_travel)
        guide_main_view.set_action("delete_selected_travel", self.delete_travel)

        create_experience_view.set_action("save", self.save_new_travel)
        create_experience_view.set_action("back", lambda: self.app.show_window("guide_main_view"))

        experience_edit_view.set_action("save", self.save_edited_travel)
        experience_edit_view.set_action("back", lambda: self.app.show_window("guide_main_view"))

    def show_create_travel(self):
        create_experience_view = self.app.get_window("create_experience_view")
        create_experience_view.clear_fields()
        self.app.show_window("create_experience_view")

    def save_new_travel(self, travel_data):
        success = self.travel_service.add_travel(travel_data)
        if success:
            print("Travel created successfully!")
            self.app.show_window("guide_main_view")
        else:
            print("Failed to create travel.")
            create_experience_view = self.app.get_window("create_experience_view")
            create_experience_view.show_error("Failed to create travel. Try again.")

    def show_edit_travel(self, selected_travel):
        if selected_travel:
            experience_edit_view = self.app.get_window("experience_edit_view")
            experience_edit_view.set_experience_data(selected_travel)
            self.app.show_window("experience_edit_view")
        else:
            print("No travel selected!")

    def save_edited_travel(self, updated_data):
        success = self.travel_service.update_travel(updated_data)
        if success:
            print("Travel updated successfully!")
            self.app.show_window("guide_main_view")
        else:
            print("Failed to update travel.")
            experience_edit_view = self.app.get_window("experience_edit_view")
            experience_edit_view.show_error("Failed to update travel. Try again.")

    def delete_travel(self, selected_travel):
        if selected_travel:
            success = self.travel_service.delete_travel(selected_travel)
            if success:
                print("Travel deleted successfully!")
                guide_main_view = self.app.get_window("guide_main_view")
                guide_main_view.refresh_table()
            else:
                print("Failed to delete travel.")
        else:
            print("No travel selected!")
