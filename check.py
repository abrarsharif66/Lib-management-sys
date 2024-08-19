class CheckoutManager:
    def __init__(self):
        """
        Initializes a new CheckoutManager instance.
        """
        self.checkouts = []

    def checkout_book(self, user_id, book_manager, isbn):
        """
        Records a book checkout by a user.

        :param user_id: Unique ID of the user
        :param book_manager: Instance of BookManager to access books
        :param isbn: ISBN number of the book
        """
        book = book_manager.find_book_by_isbn(isbn)
        if book and book.available:
            self.checkouts.append({"user_id": user_id, "isbn": isbn})
            book.copies -= 1  # Decrease the number of copies
            book_manager.update_availability(book)
            print("Book checked out successfully.")
        else:
            print("Book is not available for checkout.")

    def list_checkouts(self):
        """
        Lists all the book checkouts.
        """
        if not self.checkouts:
            print("No checkouts available.")
            return
        for checkout in self.checkouts:
            print(f"User ID: {checkout['user_id']}, ISBN: {checkout['isbn']}")

    def return_book(self, user_id, book_manager, isbn):
        """
        Records the return of a book by a user.

        :param user_id: Unique ID of the user
        :param book_manager: Instance of BookManager to access books
        :param isbn: ISBN number of the book
        """
        for checkout in self.checkouts:
            if checkout['user_id'] == user_id and checkout['isbn'] == isbn:
                self.checkouts.remove(checkout)
                book = book_manager.find_book_by_isbn(isbn)
                if book:
                    book.copies += 1  # Increase the number of copies
                    book_manager.update_availability(book)
                    print("Book returned successfully.")
                return
        print("Checkout record not found.")
