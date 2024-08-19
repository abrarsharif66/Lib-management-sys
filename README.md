# Library Management System


### `book.py`
Contains the `Book` and `BookManager` classes:
- `Book`: Represents a book with attributes like title, author, ISBN, number of copies, and availability.
- `BookManager`: Manages operations related to books, such as adding and listing books.

### `user.py`
Contains the `User` and `UserManager` classes:
- `User`: Represents a user with attributes like name and user ID.
- `UserManager`: Manages operations related to users, such as adding and listing users.

### `check.py`
Contains the `CheckoutManager` class:
- `CheckoutManager`: Manages book checkouts and returns.

### `storage.py`
Contains the `StorageManager` class:
- `StorageManager`: Handles loading and saving data to CSV files.

### `main.py`
The entry point of the application:
- Contains the main loop, user interface, and logic to manage the library system.


Run the `main.py` file to start the system.

   ```bash
   python main.py
   ```

## How to Use

1. **Add a Book:**
   - Choose option `1` in the main menu.
   - Enter the title, author, ISBN, and the number of copies.

2. **List All Books:**
   - Choose option `2` to display all the books in the library.

3. **Add a User:**
   - Choose option `3` to add a new user.
   - Enter the user's name and ID.

4. **List All Users:**
   - Choose option `4` to display all the users.

5. **Check Out a Book:**
   - Choose option `5` to check out a book.
   - Enter the user's ID and the ISBN of the book.

6. **Return a Book:**
   - Choose option `6` to return a book.
   - Enter the user's ID and the ISBN of the book.

7. **List All Checkouts:**
   - Choose option `7` to display all current checkouts.

8. **Exit the System:**
   - Choose option `8` to save all data and exit the system.

## Data Storage

- **Books:** Stored in `books.csv`
- **Users:** Stored in `users.csv`
- **Checkouts:** Stored in `checkouts.csv`

The system automatically saves the data to these CSV files when you exit(choose option 8).

