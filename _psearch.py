import sys
import os
import logging


def ParseCommandLine():
    parser = argparse.ArgumentParser('Python Search')

    parser.add_argument('-v', '--verbose', help="Enables Printing of Program messages", action='store_true')

    parser.add_argument('-k','--keyWords', type=ValidateFileRead, required=True, help='Specifify the file containing search words')

    parser.add_argument('-t','--srchTarget', type=ValidateFileRead, required=True, help='Specify the target file to search')

global gl_args
gl_args = parser.parse_args()
DisplayMessage("Command Line processed: Successfully")
return

def ValidateFileRead(theFile):
    # Check validation of path
    if not os.path.exists(theFile):
        raise argparse.ArgumentTypeError('File Does not exist')
    #validate path readable
    if os.access(theFile, os.R_OK):
        return theFile
    else
        raise argparse.ArgumentTypeError('File is not readable')

def SearchWords():
    searchWords=set()
    try:
        fileWords = open(gl_args.keyWords)