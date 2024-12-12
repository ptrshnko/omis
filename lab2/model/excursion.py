class Excursion:
    def __init__(self, excursion_id, name, author, place, theme, age):
        self.excursion_id = excursion_id
        self.name = name
        self.slide_list = []
        self.mark_list = []
        self.complete_time = 0
        self.author = author
        self.age = age
        self.theme = theme
        self.place = place

    def add_slide(self, slide):
        self.slide_list.append(slide)

    def add_mark(self, mark):
        self.mark_list.append(mark)

    def __str__(self):
        return f"Excursion(id={self.excursion_id}, name={self.name}, place={self.place})"