# Lab Exercise 15: Library Management System
# Student: Niranjan P G | USN: 25BTRAD074

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"[{self.book_id}] '{self.title}' by {self.author} ({status})"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Catalogued: {book.title}")

    def issue_book(self, book_id, borrower):
        b = self.books.get(book_id)
        if b and not b.is_issued:
            b.is_issued = True
            print(f"Success: '{b.title}' issued to {borrower}.")
        else:
            print(f"Unavailable: Book {book_id} is already issued.")

    def return_book(self, book_id):
        b = self.books.get(book_id)
        if b and b.is_issued:
            b.is_issued = False
            print(f"Success: '{b.title}' has been returned.")

    def display(self):
        print(f"\n--- {self.name} Catalogue ---")
        for b in self.books.values():
            print(f" {b}")

if __name__ == "__main__":
    print("=== Library Management System (OOP) ===")
    lib = Library("SET Technical Library")
    lib.add_book(Book("B101", "Learning Python", "Mark Lutz"))
    lib.add_book(Book("B102", "Data Science Handbook", "Jake VanderPlas"))
    lib.display()
    lib.issue_book("B101", "Niranjan P G")
    lib.issue_book("B101", "Aarav Sharma")
    lib.return_book("B101")
    lib.display()
