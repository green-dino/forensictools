import os
import csv
import json

class DataStorageManager:
    def __init__(self, storage_file_path="data_storage.json"):
        self.storage_file_path = storage_file_path
        self.data_storage = {}

    def csv_to_dictionary(self, file_path):
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            sheet_data = [row for row in reader]
        return sheet_data

    def save_data_storage(self):
        with open(self.storage_file_path, 'w') as json_file:
            json.dump(self.data_storage, json_file)

    def load_data_storage(self):
        if os.path.exists(self.storage_file_path):
            with open(self.storage_file_path, 'r') as json_file:
                self.data_storage = json.load(json_file)

    def print_dictionary_keys(self):
        print("Dictionary keys:")
        for key in self.data_storage:
            print("- " + key)

    def process_folder(self, folder_path):
        if os.path.exists(self.storage_file_path):
            self.load_data_storage()
            print("Loaded data storage from file.")
        else:
            self.data_storage = {}

            for filename in os.listdir(folder_path):
                if filename.endswith(".csv"):
                    file_path = os.path.join(folder_path, filename)
                    sheet_name = os.path.splitext(filename)[0]

                    sheet_data = self.csv_to_dictionary(file_path)
                    self.data_storage[sheet_name] = {"data": sheet_data}

            self.save_data_storage()
            print("Saved data storage to file.")

    def list_available_sheets(self):
        print("Available sheet names:")
        for sheet_name in self.data_storage.keys():
            print("- " + sheet_name)

    def access_sheet_data(self, sheet_name):
        if sheet_name in self.data_storage:
            sheet_data = self.data_storage[sheet_name]["data"]
            print(f"Data from sheet '{sheet_name}':")

            for row_data in sheet_data:
                print(row_data)
        else:
            print("Sheet name not found in data storage.")

    def view_components_in_data_storage(self):
        print("\nComponents in data storage:")
        self.print_dictionary_keys()

if __name__ == "__main__":
    manager = DataStorageManager()

    folder_path = input("Enter the path of the folder containing CSV files: ")
    manager.process_folder(folder_path)

    manager.list_available_sheets()

    sheet_name_to_access = input("Enter the sheet name you want to access: ")
    manager.access_sheet_data(sheet_name_to_access)

    manager.view_components_in_data_storage()
