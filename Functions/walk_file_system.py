
# Python Standard Libaries 
import os
import hashlib

# This script is useful for quickly obtaining a list of files within a specified directory and can be a helpful tool for various file management and analysis tasks.
# Users can customize the script to include additional file attributes or sort the table differently based on their specific requirements.

# Python 3rd Party Libraries
from prettytable import PrettyTable     # pip install prettytable

# Psuedo Constants
DIR = input("Enter Directory Path: ")

# Start of the Script
print("Walking: ", DIR, "\n")

tbl = PrettyTable(['FileName','FileSize'])  

for currentRoot, dirList, fileList in os.walk(DIR):
    '''
    print()
    print("root:    ", currentRoot)
    print("dirs:    ", dirList)
    print("files: : ", fileList)
    print()
    '''

    for nextFile in fileList:
        
        fullPath = os.path.join(currentRoot, nextFile)
        absPath = os.path.abspath(fullPath)
        
        print("="*40)
        print("FilePath: ", absPath)            # Display absolute File Path
        
        stats = os.stat(absPath)
        fileSize = stats.st_size
        
        tbl.add_row( [ absPath, fileSize] ) 
        
tbl.align = "l" # align the columns left justified

# display the table
print (tbl.get_string(sortby="FileSize", reversesort=True))


print("\nScript-End\n")