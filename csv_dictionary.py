import os
import csv
import json

def csv_to_dictionary(file_path):
    data_dictionary = {}

    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        sheet_data = [row for row in reader]

    return sheet_data

def save_data_storage(data_storage, file_path):
    with open(file_path, 'w') as json_file:
        json.dump(data_storage, json_file)

def load_data_storage(file_path):
    with open(file_path, 'r') as json_file:
        data_storage = json.load(json_file)
    return data_storage

def print_dictionary_keys(data_dict):
    print("Dictionary keys:")
    for key in data_dict:
        print("- " + key)

def main():
    folder_path = input("Enter the path of the folder containing CSV files: ")
    storage_file_path = "data_storage.json"  # File to save and load data_storage
    
    if os.path.exists(storage_file_path):
        data_storage = load_data_storage(storage_file_path)
        print("Loaded data storage from file.")
    else:
        data_storage = {}  # Create a dictionary to store all data
        
        for filename in os.listdir(folder_path):
            if filename.endswith(".csv"):
                file_path = os.path.join(folder_path, filename)
                sheet_name = os.path.splitext(filename)[0]
                
                sheet_data = csv_to_dictionary(file_path)
                data_storage[sheet_name] = {"data": sheet_data}  # Store the data dictionary
        
        save_data_storage(data_storage, storage_file_path)
        print("Saved data storage to file.")

    print("Available sheet names:")
    for sheet_name in data_storage.keys():
        print("- " + sheet_name)

    # Access data from the 'data_storage' dictionary after the 'main' function has executed
    sheet_name_to_access = input("Enter the sheet name you want to access: ")
    
    if sheet_name_to_access in data_storage:
        sheet_data = data_storage[sheet_name_to_access]["data"]
        print(f"Data from sheet '{sheet_name_to_access}':")
        
        for row_data in sheet_data:
            print(row_data)
    else:
        print("Sheet name not found in data storage.")
    
    # View the components in data storage
    print("\nComponents in data storage:")
    print_dictionary_keys(data_storage)

if __name__ == "__main__":
    main()
