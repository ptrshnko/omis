from model.database import Database
from model.mark import Mark


class MarkRepository:
    def __init__(self):
        self.database = Database()

    def create_mark(self, mark: Mark):
        self.database.save(mark.mark_id, mark)

    def update_mark(self, mark: Mark):
        if self.database.get(mark.mark_id):
            self.database.save(mark.mark_id, mark)
        else:
            print("Mark not found")

    def delete_mark(self, mark_id: str):
        self.database.delete(mark_id)

    def get_mark(self, mark_id: str):
        return self.database.get(mark_id)
