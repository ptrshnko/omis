from model.database import Database
from model.travel import Travel


class TravelRepository:
    def __init__(self):
        self.database = Database()

    def create_travel(self, travel: Travel):
        self.database.save(travel.travel_id, travel)

    def update_travel(self, travel: Travel):
        if self.database.get(travel.travel_id):
            self.database.save(travel.travel_id, travel)
        else:
            print("Travel not found")

    def delete_travel(self, travel_id: str):
        self.database.delete(travel_id)

    def get_travel(self, travel_id: str):
        return self.database.get(travel_id)

    def find_by_name(self, name: str):
        return [travel for travel in self.database.data.values() if isinstance(travel, Travel) and travel.name == name]
