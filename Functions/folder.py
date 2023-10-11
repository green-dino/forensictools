import os
import hashlib
from datetime import datetime
from prettytable import PrettyTable

def analyze_folder_properties(target_folder):
    print("Walking: ", target_folder, "\n")
    
    tbl = PrettyTable(['FilePath', 'FileSize', 'Modified Time', 'Access Time', 'Created Time', 'SHA-256 Hash'])
    
    for current_root, dir_list, file_list in os.walk(target_folder):
        for next_file in file_list:
            full_path = os.path.join(current_root, next_file)
            abs_path = os.path.abspath(full_path)
            file_size = os.path.getsize(abs_path)
            
            # MAC Times (in human-readable form)
            modified_time = os.path.getmtime(abs_path)
            accessed_time = os.path.getatime(abs_path)
            created_time = os.path.getctime(abs_path)
            
            modified_time_str = datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d %H:%M:%S')
            accessed_time_str = datetime.fromtimestamp(accessed_time).strftime('%Y-%m-%d %H:%M:%S')
            created_time_str = datetime.fromtimestamp(created_time).strftime('%Y-%m-%d %H:%M:%S')
            
            # SHA-256 Hash value of the content of each file
            sha256_hash = hashlib.sha256()
            with open(abs_path, "rb") as file:
                while chunk := file.read(8192):
                    sha256_hash.update(chunk)
            sha256_hash_value = sha256_hash.hexdigest()
            
            tbl.add_row([abs_path, file_size, modified_time_str, accessed_time_str, created_time_str, sha256_hash_value])
    
    tbl.align = "l"  # align the columns left justified
    # display the table
    print(tbl.get_string(sortby="FileSize", reversesort=True))
    
    print("\nScript-End\n")

if __name__ == "__main__":
    target_folder = input("Enter Target Folder: ")
    analyze_folder_properties(target_folder)
