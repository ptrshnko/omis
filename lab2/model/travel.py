class Travel:
    def __init__(self, travel_id, name, author, country):
        self.travel_id = travel_id
        self.name = name
        self.slide_list = []
        self.mark_list = []
        self.excursion_list = []
        self.complete_time = 0
        self.author = author
        self.country = country

    def add_slide(self, slide):
        self.slide_list.append(slide)

    def add_mark(self, mark):
        self.mark_list.append(mark)

    def add_excursion(self, excursion):
        self.excursion_list.append(excursion)

    def __str__(self):
        return f"Travel(id={self.travel_id}, name={self.name}, country={self.country})"
