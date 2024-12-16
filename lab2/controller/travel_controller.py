from view.guide_main_view import guide_main_view
from view.tourist_main_view import tourist_main_view


class TravelController:
    def __init__(self, app):
        self.app = app


    def show_tourist_main(self):
        tourist_main_view(
            self.app.root,
            view_profile=self.app.show_profile,
            apply_filters=self.app.apply_filters,
            start_viewing=lambda selected_item: self.app.show_experience_start_page(selected_item),
        )

    def show_guide_main(self):
        guide_main_view(
            self.app.root,
            edit_selected=self.app.show_experience_edit_page,
            delete_selected=self.app.handle_delete_experience,
            create_new=self.app.show_create_experience,
            go_to_profile=self.app.show_profile,
        )

