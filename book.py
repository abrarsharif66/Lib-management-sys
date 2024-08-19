class Book:
    def __init__(self, title, author, isbn, copies, available=None):
        """
        Initializes a new Book instance.

        :param title: Title of the book
        :param author: Author of the book
        :param isbn: ISBN number of the book
        :param copies: Number of copies of the book
        :param available: Availability of the book (optional)
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = int(copies)  # Ensure copies is an integer
        self.available = available if available is not None else self.copies > 0  # Book is available if copies > 0

    def __str__(self):
        """
        Returns a string representation of the book.

        :return: String representation of the book
        """
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}, Available: {'Yes' if self.available else 'No'}"

# Class to manage book-related operations
class BookManager:
    def __init__(self):
    
        #Initializes a new BookManager instance.
        
        self.books = []

    def add_book(self, title, author, isbn, copies):
        
        #Adds a new book to the book list.
        book = Book(title, author, isbn, copies)
        self.books.append(book)
        print("Book added successfully.")

    def list_books(self):
        
        #Lists all the books in the library.
        
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            print(book)

    def find_book_by_isbn(self, isbn):
        
        #Finds a book by its ISBN number.
        
        for book in self.books:
            if book.isbn == isbn:
                return book
        print("Book not found.")
        return None

    def remove_book(self, isbn):
        """
        Removes a book from the library by its ISBN number.

        """
        book = self.find_book_by_isbn(isbn)
        if book:
            self.books.remove(book)
            print("Book removed successfully.")
        else:
            print("Book could not be removed.")

    def update_availability(self, book):
        """
        Updates the availability status of a book based on the number of copies.

        
        """
        book.available = book.copies > 0
