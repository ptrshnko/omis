from repository.travel_repository import TravelRepository
from model.travel import Travel

class TravelService:
    def __init__(self, travel_repository: TravelRepository):
        self.travel_repository = travel_repository

    def create_travel(self, travel: Travel):
        self.travel_repository.create_travel(travel)

    def update_travel(self, travel: Travel):
        self.travel_repository.update_travel(travel)

    def delete_travel(self, travel_id: str):
        self.travel_repository.delete_travel(travel_id)

    def find_by_name(self, name: str):
        return self.travel_repository.find_by_name(name)
