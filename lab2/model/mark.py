class Mark:
    def __init__(self, mark_id, num, author):
        self.mark_id = mark_id
        self.num = num
        self.author = author

    def __str__(self):
        return f"Mark(id={self.mark_id}, num={self.num}, author={self.author})"
