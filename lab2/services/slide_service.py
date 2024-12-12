from repository.slide_repository import SlideRepository
from model.slide import Slide

class SlideService:
    def __init__(self, slide_repository: SlideRepository):
        self.slide_repository = slide_repository

    def create_slide(self, slide: Slide):
        self.slide_repository.create_slide(slide)

    def update_slide(self, slide: Slide):
        self.slide_repository.update_slide(slide)

    def delete_slide(self, slide_id: str):
        self.slide_repository.delete_slide(slide_id)
