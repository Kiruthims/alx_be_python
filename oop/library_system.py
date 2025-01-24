class Book:
    def __init__(self, title: str, author: str):
        self.title = title  # Title of the book
        self.author = author  # Author of the book

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)  # Initialize title and author from Book
        self.file_size = file_size  # Specific to EBook

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)  # Initialize title and author from Book
        self.page_count = page_count  # Specific to PrintBook

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []  # List to store book objects

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

