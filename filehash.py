'''
File Hashing 

'''


import os        # Python standard library os/file system methods
import hashlib   # Python standard library hashlib
import sys       # Python standard library system specifics and functions
import time 

#python 3rd Party Library
from prettytable import PrettyTable # pip install prettytable 

while True:
    fileToHash = input("\nFile to Hash >>> " )
    if os.path.isfile(fileToHash):
        break
    else:
        print("\nInvalid File ... Please Try Again")
        

tbl = PrettyTable(['Path','Status','FileSize','LastModified','LastAccess','Created','SHA-256 HASH','Error Info'])


#Pseuedo Constants
DIR = input("Enter Directory Path: ")



try:
    print("\nAttempting to hash file: ", fileToHash)
    
    with open(fileToHash, 'rb') as target:
        
        fileContents = target.read()
        
        sha512Obj = hashlib.sha512()
        sha512Obj.update(fileContents)
        hexDigest = sha512Obj.hexdigest()

        print("\n\n",fileToHash, " SHA-512 Hex Digest = ", hexDigest, "\n\n")

except Exception as err:
    sys.exit("\nException: "+str(err))
    
print("Script Done")
