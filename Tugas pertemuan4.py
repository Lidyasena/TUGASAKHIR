class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book added: {new_book}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    print(f"Sorry, '{book.title}' is already borrowed.")
                else:
                    book.is_borrowed = True
                    print(f"You have borrowed: {book}")
                return
        print(f"Sorry, '{title}' is not available in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"You have returned: {book}")
                else:
                    print(f"'{book.title}' was not borrowed.")
                return
        print(f"Sorry, '{title}' is not part of this library.")

    def display_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            print("Library books:")
            for book in self.books:
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f"{book} - {status}")

# Example usage
if __name__ == "__main__":
    library = Library()

    # Adding books
    library.add_book("The Catcher in the Rye", "J.D. Salinger")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")

    # Display books
    library.display_books()
    print()

    # Borrowing books
    library.borrow_book("1984")
    library.borrow_book("The Catcher in the Rye")
    library.borrow_book("1984")  # Trying to borrow again

    # Display books
    library.display_books()
    print()

    # Returning books
    library.return_book("1984")
    library.return_book("The Catcher in the Rye")

    # Display books
    library.display_books()
    print()
