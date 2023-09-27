# Python Standard Libraries
import os
import sys  # System Methods
import hashlib
import argparse
from datetime import datetime

# The script provides a quick way to analyze file properties in a given folder, making it useful for tasks like file inventory, monitoring, or audit.
# You can further customize or extend the script to include additional information or perform specific actions on the gathered data.
# Ensure that you have necessary permissions to access the target folder and its files.

# Python 3rd Party Libraries
from prettytable import PrettyTable  # pip install prettytable

# Psuedo Constants

targetFolder = input("Enter Target Folder: ")

# Start of the Script
print("Walking: ", targetFolder, "\n")

tbl = PrettyTable(['FilePath', 'FileSize', 'Modified Time', 'Access Time', 'Created Time', 'SHA-256 Hash'])

for currentRoot, dirList, fileList in os.walk(targetFolder):

    for nextFile in fileList:

        fullPath = os.path.join(currentRoot, nextFile)
        absPath = os.path.abspath(fullPath)
        fileSize = os.path.getsize(absPath)

        # MAC Times (in human-readable form)
        modified_time = os.path.getmtime(absPath)
        accessed_time = os.path.getatime(absPath)
        created_time = os.path.getctime(absPath)

        modified_time_str = datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d %H:%M:%S')
        accessed_time_str = datetime.fromtimestamp(accessed_time).strftime('%Y-%m-%d %H:%M:%S')
        created_time_str = datetime.fromtimestamp(created_time).strftime('%Y-%m-%d %H:%M:%S')

        # SHA-256 Hash value of the content of each file
        sha256_hash = hashlib.sha256()
        with open(absPath, "rb") as file:
            while chunk := file.read(8192):
                sha256_hash.update(chunk)
        sha256_hash_value = sha256_hash.hexdigest()

        tbl.add_row([absPath, fileSize, modified_time_str, accessed_time_str, created_time_str, sha256_hash_value])

tbl.align = "l"  # align the columns left justified
# display the table
print(tbl.get_string(sortby="FileSize", reversesort=True))

print("\nScript-End\n")
