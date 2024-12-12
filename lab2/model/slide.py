class Slide:
    def __init__(self, slide_id, text, image=None, video=None):
        self.slide_id = slide_id
        self.text = text
        self.image = image
        self.video = video

    def __str__(self):
        return f"Slide(id={self.slide_id}, text={self.text[:30]}...)"

