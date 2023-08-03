#The code begins
class Book:
    def _init_(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def _init_(self):
        self.books = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        print(f"Book '{title}' added to the library.")

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")

    def search_book_by_title(self, title):
        matching_books = [book for book in self.books if book.title.lower() == title.lower()]
        if matching_books:
            print(f"Found {len(matching_books)} book(s) with the title '{title}':")
            for book in matching_books:
                print(f"Author: {book.author}, ISBN: {book.isbn}")
        else:
            print(f"No books found with the title '{title}'.")

    def search_book_by_author(self, author):
        matching_books = [book for book in self.books if book.author.lower() == author.lower()]
        if matching_books:
            print(f"Found {len(matching_books)} book(s) by the author '{author}':")
            for book in matching_books:
                print(f"Title: {book.title}, ISBN: {book.isbn}")
        else:
            print(f"No books found by the author '{author}'.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book by Title")
        print("4. Search Book by Author")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            library.add_book(title, author, isbn)
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            title = input("Enter the title to search: ")
            library.search_book_by_title(title)
        elif choice == "4":
            author = input("Enter the author to search: ")
            library.search_book_by_author(author)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
