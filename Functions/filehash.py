import os
import hashlib
import time
from prettytable import PrettyTable

class FileHasher:
    def __init__(self):
        self.tbl = PrettyTable(['Path', 'Status', 'FileSize', 'LastModified', 'LastAccess', 'Created', 'SHA-512 HASH', 'Error Info'])

    def hash_file(self, file_path):
        try:
            with open(file_path, 'rb') as target:
                file_contents = target.read()
                sha512_obj = hashlib.sha512()
                sha512_obj.update(file_contents)
                hex_digest = sha512_obj.hexdigest()
                return hex_digest
        except Exception as err:
            return str(err)

    def process_directory(self, directory_path):
        for root, _, files in os.walk(directory_path):
            for file_name in files:
                file_to_hash = os.path.join(root, file_name)
                if os.path.isfile(file_to_hash):
                    print("\nAttempting to hash file:", file_to_hash)
                    file_info = os.stat(file_to_hash)
                    file_size = file_info.st_size
                    last_modified = time.ctime(file_info.st_mtime)
                    last_access = time.ctime(file_info.st_atime)
                    created = time.ctime(file_info.st_ctime)
                    hash_value = self.hash_file(file_to_hash)
                    error_info = ""
                    if isinstance(hash_value, str):
                        error_info = hash_value
                        hash_value = "Error"
                    self.tbl.add_row([file_to_hash, "Success", file_size, last_modified, last_access, created, hash_value, error_info])
                else:
                    self.tbl.add_row([file_to_hash, "Invalid File", "-", "-", "-", "-", "-", ""])

    def print_result_table(self):
        print(self.tbl)

def hash_files_in_directory(directory_path):
    file_hasher = FileHasher()
    if os.path.isdir(directory_path):
        file_hasher.process_directory(directory_path)
        file_hasher.print_result_table()
    else:
        print("\nInvalid Directory")

if __name__ == "__main__":
    while True:
        directory_path = input("\nEnter the directory path to hash files >>> ")
        if os.path.isdir(directory_path):
            break
        else:
            print("\nInvalid Directory... Please Try Again")

    hash_files_in_directory(directory_path)
    print("Script Done")
