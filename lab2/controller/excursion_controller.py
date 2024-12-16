from view.content_viewer import content_viewer
from view.create_experience_view import create_experience_view
from view.experience_edit_view import experience_edit_view


class ExcursionController:

    def __init__(self, app):
        self.app = app

    def show_experience_edit_page(self, experience=None):
        if experience:
            experience_edit_view(
                self.app.root,
                experience_data={
                    "name": experience[0],
                    "type": experience[1],
                    "country": experience[2],
                    "theme": experience[3],
                    "rating": experience[4],
                },
                handle_save=self.app.handle_save_experience_edit,
                go_back=self.app.show_guide_main
            )
        else:
            print("No experience selected!")

    def show_experience_start_page(self, experience=None):
        if experience:
            print(f"Starting experience: {experience}")
            self.show_content_viewer()
        else:
            print("No experience selected! Returning to main screen.")
            self.app.show_tourist_main()

    def handle_delete_experience(self, experience=None, table=None):
        if experience:
            print(f"Deleting experience: {experience}")
            for row in table.get_children():
                if table.item(row)["values"] == experience:
                    table.delete(row)
                    break
        else:
            print("No experience selected!")

    def apply_filters(self, *args):
        print(f"Filters applied: {args}")

    def handle_save_experience_edit(self, updated_data):
        print(f"Updated experience: {updated_data}")
        self.app.show_guide_main()

    def handle_save_experience(self, name, description, age, theme):
        print(f"Saved Experience: {name}, {description}, {age}, {theme}")

    def show_content_viewer(self):
        slides = self.app.get_slides()
        content_viewer(self.app.root, slides=slides, go_back=self.app.show_tourist_main)

    def show_create_experience(self):
        create_experience_view(
            self.app.root,
            handle_save=self.handle_save_experience,
            go_back=self.app.show_guide_main
        )
