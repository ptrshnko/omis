class SlideController:
    def __init__(self, app):
        self.app = app


    @staticmethod
    def get_slides():
        return [
            {"text": "Welcome to the Louvre Tour!", "image": "luvr.jpg", "video": "intro.mp4"},
            {"text": "The Mona Lisa is one of the most famous paintings in the world.", "image": "mona-lisa.jpg"},
            {"text": "The Venus de Milo is a celebrated ancient Greek statue.", "video": "venus.mp4"},
        ]
