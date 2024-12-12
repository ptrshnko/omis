from model.database import Database
from model.slide import Slide


class SlideRepository:
    def __init__(self):
        self.database = Database()

    def create_slide(self, slide: Slide):
        self.database.save(slide.slide_id, slide)

    def update_slide(self, slide: Slide):
        if self.database.get(slide.slide_id):
            self.database.save(slide.slide_id, slide)
        else:
            print("Slide not found")

    def delete_slide(self, slide_id: str):
        self.database.delete(slide_id)

    def get_slide(self, slide_id: str):
        return self.database.get(slide_id)
