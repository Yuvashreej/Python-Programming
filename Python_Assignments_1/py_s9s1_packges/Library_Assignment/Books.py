
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True   # we are giving default as True of this attribute.

    def show_info(self):
        print("Book: ",self.title," Author :", self.author, "Available: ",self.is_available)
