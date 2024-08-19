class User:
    def __init__(self, name, user_id):
        """
        Initializes a new User instance.

        :param name: Name of the user
        :param user_id: Unique ID for the user
        """
        self.name = name
        self.user_id = user_id

    def __str__(self):
        """
        Returns a string representation of the user.

        :return: String representation of the user
        """
        return f"Name: {self.name}, User ID: {self.user_id}"


# Class to manage user-related operations
class UserManager:
    def __init__(self):
        """
        Initializes a new UserManager instance.
        """
        self.users = []

    def add_user(self, name, user_id):
        """
        Adds a new user to the user list.

        :param name: Name of the user
        :param user_id: Unique ID for the user
        """
        user = User(name, user_id)
        self.users.append(user)
        print("User added successfully.")

    def list_users(self):
        """
        Lists all the users in the system.
        """
        if not self.users:
            print("No users available.")
            return
        for user in self.users:
            print(user)

    def find_user_by_id(self, user_id):
        """
        Finds a user by their user ID.

        :param user_id: Unique ID for the user
        :return: User instance if found, None otherwise
        """
        for user in self.users:
            if user.user_id == user_id:
                return user
        print("User not found.")
        return None

    def remove_user(self, user_id):
        """
        Removes a user from the system by their user ID.

        :param user_id: Unique ID for the user
        """
        user = self.find_user_by_id(user_id)
        if user:
            self.users.remove(user)
            print("User removed successfully.")
        else:
            print("User could not be removed.")
