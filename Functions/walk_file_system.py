import os
import hashlib
from prettytable import PrettyTable

def list_files_in_directory(directory):
    print("Walking: ", directory, "\n")

    tbl = PrettyTable(['FileName', 'FileSize'])

    for currentRoot, dirList, fileList in os.walk(directory):
        for nextFile in fileList:
            fullPath = os.path.join(currentRoot, nextFile)
            absPath = os.path.abspath(fullPath)

            print("=" * 40)
            print("FilePath: ", absPath)  # Display absolute File Path

            stats = os.stat(absPath)
            fileSize = stats.st_size

            tbl.add_row([absPath, fileSize])

    tbl.align = "l"  # align the columns left justified

    # display the table
    print(tbl.get_string(sortby="FileSize", reversesort=True))

    print("\nScript-End\n")

if __name__ == "__main__":
    dir_path = input("Enter Directory Path: ")
    list_files_in_directory(dir_path)
