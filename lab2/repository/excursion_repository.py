from model.database import Database
from model.excursion import Excursion


class ExcursionRepository:
    def __init__(self):
        self.database = Database()

    def create_excursion(self, excursion: Excursion):
        self.database.save(excursion.excursion_id, excursion)

    def update_excursion(self, excursion: Excursion):
        if self.database.get(excursion.excursion_id):
            self.database.save(excursion.excursion_id, excursion)
        else:
            print("Excursion not found")

    def delete_excursion(self, excursion_id: str):
        self.database.delete(excursion_id)

    def get_excursion(self, excursion_id: str):
        return self.database.get(excursion_id)

    def find_by_name(self, name: str):
        return [excursion for excursion in self.database.data.values() if isinstance(excursion, Excursion) and excursion.name == name]
