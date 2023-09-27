''' IMPORT STANDARD LIBRARIES '''
import os       # File System Methods
import sys      # System Methods
import time     # Time Conversion Methods
from datetime import datetime
import hashlib
import csv

''' IMPORT 3RD PARTY LIBRARIES '''
from prettytable import PrettyTable

''' DEFINE PSEUDO CONSTANTS '''

# NONE

''' LOCAL FUNCTIONS '''

class FileInspectionError(Exception):
    pass

'''Define Constants for Block Size and file types
'''

# Define constants for block size and file types
BLOCK_SIZE = 4096
FILE_TYPE_FILE = "File"
FILE_TYPE_DIRECTORY = "Directory"
FILE_TYPE_LINK = "Link"
FILE_TYPE_UNKNOWN = "Unknown"


def GetFileMetaData(fileName):
    ''' 
        obtain filesystem metadata
        from the specified file
        specifically, fileSize and MAC Times
        
        return True, None, fileSize and MacTimeList
    '''
    try:
        metaData = os.stat(fileName)   # Use the stat method to obtain meta data
        fileSize = metaData.st_size    # Extract fileSize and MAC Times
        timeLastAccess = metaData.st_atime
        timeLastModified = metaData.st_mtime
        timeCreated = metaData.st_ctime
        
        macTimeList = [timeLastModified, timeCreated, timeLastAccess]   # Group the MAC Times in a List
        return True, None, fileSize, macTimeList
    
    except Exception as err:
        return False, str(err), None, None

def CalculateSHA256(filePath):
    ''' 
        calculate the SHA-256 hash value
        of the content of the file
    '''
    try:
        sha256_hash = hashlib.sha256()
        with open(filePath, "rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(BLOCK_SIZE), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as err:
        return str(err)

def inspect_directory(directory):
    ''' 
        Recursively inspect the specified directory and its subdirectories
    '''
    try:
        fileList = os.listdir(directory)
        for eachFile in fileList:
            path = os.path.join(directory, eachFile)
            path = os.path.abspath(path)

            success, errInfo, fileSize, macList = GetFileMetaData(path)

            if success:
                modTime = datetime.fromtimestamp(macList[0]).strftime('%Y-%m-%d %H:%M:%S')
                accTime = datetime.fromtimestamp(macList[1]).strftime('%Y-%m-%d %H:%M:%S')
                creTime = datetime.fromtimestamp(macList[2]).strftime('%Y-%m-%d %H:%M:%S')

                if os.path.isfile(path):
                    fileType = "File"
                    sha256_hash = CalculateSHA256(path)
                elif os.path.isdir(path):
                    fileType = "Directory"
                    sha256_hash = "N/A"
                    inspect_directory(path)  # Recursively inspect subdirectories
                elif os.path.islink(path):
                    fileType = "Link"
                    sha256_hash = "N/A"
                else:
                    fileType = "Unknown"
                    sha256_hash = "N/A"

                resultTable.add_row([path, fileSize, modTime, accTime, creTime, sha256_hash])

            else:
                print("Fail:      ", path, "Exception =     ", errInfo)

    except Exception as err:
        print("\n\nScript Aborted     ", "Exception =     ", err)


''' LOCAL CLASSES '''
# NONE

''' MAIN ENTRY POINT '''

def main():
    print("\nWork\n")

    targetDIR = input('Enter a Directory Path i.e. c:/ >>> ')
    print()

    global resultTable
    resultTable = PrettyTable(['AbsPath', 'FileSize', 'LastModified', 'LastAccess', 'CreatedTime', 'SHA-256 HASH'])

    resultList = []

    try:
        inspect_directory(targetDIR)

        resultTable.align = "l"
        print(resultTable.get_string(sortby="FileSize", reversesort=True))

        # Save the PrettyTable as a .csv file
        with open('file_metadata.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(resultTable.field_names)
            for row in resultTable:
                csv_writer.writerow(row)

        print("File metadata saved as file_metadata.csv")

    except Exception as err:
        print("\n\nScript Aborted     ", "Exception =     ", err)



if __name__ == '__main__':
    main()
    print("Script End")
