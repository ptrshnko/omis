class Status:
    TOURIST = "Tourist"
    GUIDE = "Guide"


class User:
    def __init__(self, user_id, name, birth_year, status, password):
        self.user_id = user_id
        self.name = name
        self.birth_year = birth_year
        self.travel_list = []
        self.excursion_list = []
        self.status = status
        self.password = password

    def add_travel(self, travel):
        self.travel_list.append(travel)

    def add_excursion(self, excursion):
        self.excursion_list.append(excursion)

    def get_age(self, current_year):
        return current_year - self.birth_year

    def __str__(self):
        return f"User(id={self.user_id}, name={self.name}, status={self.status})"

