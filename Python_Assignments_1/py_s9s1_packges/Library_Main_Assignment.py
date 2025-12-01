import sys
sys.path.append("C:/Users/Yuvashree.J/Documents/Python Programming/Python Traning/Oops_concepts/Python Packages/Library_Assignment")

from Books import Book # type: ignore 
from Users import User # type: ignore
from Transaction import Transaction # type: ignore

book1 = Book("Python Basics", "Guido")
book2 = Book("Data Structures", "Turing")

user1 = User("Yuva", "student")
user2 = User("Charan", "staff")

t = Transaction()

print("=== Books ===")
book1.show_info()
book2.show_info()

print("\n=== Users ===")
user1.show_user()
user2.show_user()

print("\n=== Borrowing ===")
t.borrow_book(book1, user1)        # we are passing the "book" and "user" objects

print("\n=== After Borrow ===")
book1.show_info()

print("\n=== Returning ===")
t.return_book(book1, user1)

print("\n=== After Return ===")
book1.show_info()

 

