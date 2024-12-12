from repository.mark_repository import MarkRepository
from model.mark import Mark

class MarkService:
    def __init__(self, mark_repository: MarkRepository):
        self.mark_repository = mark_repository

    def create_mark(self, mark: Mark):
        self.mark_repository.create_mark(mark)

    def update_mark(self, mark: Mark):
        self.mark_repository.update_mark(mark)

    def delete_mark(self, mark_id: str):
        self.mark_repository.delete_mark(mark_id)
