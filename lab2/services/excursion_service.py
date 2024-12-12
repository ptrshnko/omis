from repository.excursion_repository import ExcursionRepository
from model.excursion import Excursion

class ExcursionService:
    def __init__(self, excursion_repository: ExcursionRepository):
        self.excursion_repository = excursion_repository

    def create_excursion(self, excursion: Excursion):
        self.excursion_repository.create_excursion(excursion)

    def update_excursion(self, excursion: Excursion):
        self.excursion_repository.update_excursion(excursion)

    def delete_excursion(self, excursion_id: str):
        self.excursion_repository.delete_excursion(excursion_id)

    def find_by_name(self, name: str):
        return self.excursion_repository.find_by_name(name)
