from book import BookManager, Book
from user import UserManager, User
from check import CheckoutManager
from storage import StorageManager

def main_menu():
    """
    Displays the main menu and gets the user's choice.

    :return: The user's menu choice
    """
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. List Books")
    print("3. Add User")
    print("4. List Users")
    print("5. Checkout Book")
    print("6. Return Book")
    print("7. List Checkouts")
    print("8. Exit")
    print("If you want to save the state of the changes made please select option 8 interupting the program will not save the changes into csv")

    choice = input("Enter choice: ")
    return choice

def main():
    """
    Main function to run the Library Management System.
    """
    # Create instances of the manager classes
    book_manager = BookManager()
    user_manager = UserManager()
    checkout_manager = CheckoutManager()

    # Create an instance of the storage manager with CSV files
    book_storage = StorageManager("books.csv")
    user_storage = StorageManager("users.csv")
    checkout_storage = StorageManager("checkouts.csv")

    # Load existing data from CSV files
    book_manager.books = [Book(**data) for data in book_storage.load_data()]
    user_manager.users = [User(**data) for data in user_storage.load_data()]
    checkout_manager.checkouts = checkout_storage.load_data()

    while True:
        choice = main_menu()

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            copies = int(input("Enter number of copies: "))
            book_manager.add_book(title, author, isbn, copies)

        elif choice == "2":
            book_manager.list_books()

        elif choice == "3":
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_manager.add_user(name, user_id)

        elif choice == "4":
            user_manager.list_users()

        elif choice == "5":
            user_id = input("Enter user ID: ")
            isbn = input("Enter book ISBN: ")
            checkout_manager.checkout_book(user_id, book_manager, isbn)

        elif choice == "6":
            user_id = input("Enter user ID: ")
            isbn = input("Enter book ISBN: ")
            checkout_manager.return_book(user_id, book_manager, isbn)

        elif choice == "7":
            checkout_manager.list_checkouts()

        elif choice == "8":
            # Save all data to CSV files before exiting
            book_storage.save_data([vars(book) for book in book_manager.books], ["title", "author", "isbn", "copies", "available"])
            user_storage.save_data([vars(user) for user in user_manager.users], ["name", "user_id"])
            checkout_storage.save_data(checkout_manager.checkouts, ["user_id", "isbn"])
            print("Data saved. Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
