import csv

# Class to manage data storage operations using CSV
class StorageManager:
    def __init__(self, filename):
        """
        Initializes a new StorageManager instance.

        :param filename: Name of the file to save/load data
        """
        self.filename = filename

    def save_data(self, data, headers):
        """
        Saves data to a CSV file.

        :param data: Data to be saved (should be a list of dictionaries)
        :param headers: List of headers for the CSV file
        """
        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data saved to {self.filename}.")

    def load_data(self):
        """
        Loads data from a CSV file.

        :return: Loaded data as a list of dictionaries
        """
        try:
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                data = list(reader)
                print(f"Data loaded from {self.filename}.")
                return data
        except FileNotFoundError:
            print(f"{self.filename} not found. Starting with an empty data set.")
            return []
