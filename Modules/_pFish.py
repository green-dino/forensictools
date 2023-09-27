import os
import stat
import time
import hashlib
import argparse
import csv
import logging

# Parse Command Line Arguments
# The script takes various command-line arguments for configuring its behavior, including specifying the hashing algorithm (MD5, SHA256, or SHA512), root path for hashing, and report path.

# WalkPath Function
# This function traverses the directory specified by the root path and calculates file hashes using the selected hashing algorithm. It also generates a CSV report containing file details and hash values.

# Validation Functions
# The script includes functions for validating directories (whether they exist, are readable, or writeable).

# HashFile Function
# This function calculates file hashes and collects file metadata such as size, timestamps, owner, and group. It supports MD5, SHA256, and SHA512 hashing algorithms.

# DisplayMessage Function
# A simple function to display messages (replace with your preferred logging method).

# _CSVWriter Class
# A class for writing data to a CSV file. It initializes the CSV file, writes rows of data, and closes the file.


log = logging.getLogger('main._pfish')

# Parse Command Line >>>

def ParseCommandLine():
    global gl_args
    global gl_hashtype

    parser = argparse.ArgumentParser('Python File sytem hashing p-fish')
    parser.add_argument('-v', '-verbose', help= 'progress messages', action='store_true')

    # group selection is mutually exclusive and required
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--md5', help='Specifies MD5 ', action='store_true')
    group.add_argument('--sha256', help='Specifies SHA256', action='store_true')
    group.add_argument('--sha512', help='Specifices SHA 512 ', action='store_true')
    
    # path settings
    #parser.add_argument('-d', '--rootPath', type= ValidateDirectory, required=True, help="specify the root path for hashing")
    #parser.add_argument('-r', '--reportPath', type= ValidateDirectoryWriteable, required=True, help= "Specify the path for reports")

    parser.add_argument('-d', '--rootPath', type=str, required=True, help="specify the root path for hashing")
    parser.add_argument('-r', '--reportPath', type=str, required=True, help="Specify the path for reports")

    gl_args = parser.parse_args()


    if gl_args.md5:
        gl_hashtype ='MD5'
    elif gl_args.sha256:
        gl_hashtype='SHA256'
    elif gl_args.sha512:
        gl_hashtype='SHA512'
    else:
        gl_hashtype = 'Unknown'
    
   # logging.error('Unknown Hashtype')
   
    
# Parse Command Line <<<
def WalkPath():
    processCount = 0
    errorCount = 0

    log.info('Root Path:' + gl_args.rootPath)

    oCVS = _CSVWriter(gl_args.reportPath + 'fileSystemReport.csv', gl_hashtype)
    

    for root, dirs, files in os.walk(gl_args.rootPath):
        for file in files:
            fname = os.path.join(root,file)
            result = HashFile (fname, file, oCVS)

        #if successful increment count 
            if result is True:
                processCount +=1
        #if not successfull increament the errorcount   
        else:
            errorCount +=1


    oCVS.writerClose()
    return(processCount)

# Directory Validation >>>

def ValidateDirectory(theDir):
    #ensure path is a directory
    if not os.path.isdir(theDir):
        raise argparse.ArgumentTypeError('Directory does not exist')
    
    # Validate path is readable
    if os.access(theDir, os.R_OK):
        return theDir
    else:
        raise argparse.ArgumentTypeError('The Directory is not readable')
    

# Directory Validation <<<

#Directory Writable >>>

def ValidateDirectoryWriteable(theDir):
        #validate path is writable
    if os.access(theDir, os.W_OK):
        return theDir
    else:
        raise argparse.ArgumentTypeError('Directory not writeable')

#directory writeable <<<

#HashFile Function

def HashFile(theFile, simpleName, o_result):
    # Verify that the path is valid
    if not os.path.exists(theFile):
        raise FileNotFoundError('File does not exist: ' + theFile)

    # Verify that the path is not a symbolic link
    if os.path.islink(theFile):
        raise IsADirectoryError('Path is a symbolic link: ' + theFile)

    # Verify that the file is real
    if not os.path.isfile(theFile):
        raise IsADirectoryError('Not a regular file: ' + theFile)

    try:
        # Attempt to open the file
        with open(theFile, 'rb') as f:
            rd = f.read()
    except IOError:
        # If open fails, report the error
        raise IOError('Open Failed: ' + theFile)

    # Success, the file is open and we can read from it
    # File stats
    theFileStats = os.stat(theFile)
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(theFile)

    # Print the simple file name
    DisplayMessage("Processing File: " + theFile)

    # Print the size of the file in Bytes
    fileSize = str(size)

    # Print MAC Times
    modifiedTime = time.ctime(mtime)
    accessTime = time.ctime(atime)
    createdTime = time.ctime(ctime)
    ownerID = str(uid)
    groupID = str(gid)
    fileMode = bin(mode)

    # Process the file hashes
    if gl_args.md5:
        # Calculate and Print the MD5 hash
        hash = hashlib.md5()
        hash.update(rd)
        hexMD5 = hash.hexdigest()
        hashValue = hexMD5.upper()
    elif gl_args.sha256:
        # Calculate and Print the SHA256 hash
        hash = hashlib.sha256()
        hash.update(rd)
        hexSHA256 = hash.hexdigest()
        hashValue = hexSHA256.upper()
    elif gl_args.sha12:
        # Calculate and Print the SHA512 hash
        hash = hashlib.sha512()
        hash.update(rd)
        hexSHA512 = hash.hexdigest()
        hashValue = hexSHA512.upper()
    else:
        raise ValueError('Hash not Selected')

    # Write data to CSV
    o_result.writeRow([simpleName, theFile, fileSize])


# Function to display messages (replace with your preferred logging method)
def DisplayMessage(message):
    print(message)

class _CSVWriter:
    def __init__(self, fileName, hashType):
        try:
            # Construct the full path to the CSV file
            fullFilePath = os.path.join(gl_args.reportPath, fileName)
            self.csvFile = open(fullFilePath, 'w', newline='')
            # Additional initialization code here
            self.writer = csv.writer(self.csvFile)
            # delimiter =(',', quoting=csv.QUOTE_ALL)
            self.writer.writerow(('File', 'Path', 'Size'))
        except IOError:
            log.warning('Failed to open CSV file: ' + fullFilePath)

    def writeRow(self, rowData):
        try:
            self.writer.writerow(rowData)
        except IOError:
            log.warning('Failed to write to CSV File:' + self.csvFile.name)

    def writerClose(self):
        try:
            self.csvFile.close()
        except IOError:
            log.warning('Failed to close CSV file: ' + self.csvFile.name)


