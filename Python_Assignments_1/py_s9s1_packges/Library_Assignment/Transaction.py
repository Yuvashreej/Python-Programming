
class Transaction:
    def borrow_book(self, book, user):
        if book.is_available == True:
            book.is_available = False
            print(user.name, "borrowed ",book.title)
        else:
            print("Book not available")

    def return_book(self, book, user):
        book.is_available = True
        print(user.name ," returned", book.title)
