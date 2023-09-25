# psearch support functions 

import argparse
import os
import logging

log = logging.getLogger('main._psearch')

#constants
MIN_WORD = 5 # min word size in bytes
MAX_WORD = 15 # max word size in bytes
PREDECESSOR_SIZE = 32 # values to print before match found
WINDOW_SIZE = 128  # values to dump when match 

# parse command function, uses argparse 

def ParseCommanLine():
    parser = argparse.ArgumentParser('Python Search')
    parser.add_argument('-v', '--verbose', help='enables the printing of additional program messages', action='store_true')
    parser.add_argument('-k', '--keyWords', type=ValidateFileRead,
                        required=True,help='Specify the file containing search words')
    parser.add_argument('-t','--srchTarget', type=ValidateFileRead,
                        required=True, help="specifiy the target file to search")
    parser.add_argument('-m','--theMatrix', type=ValidateFileRead,
                        required=True, help='Specify the weight matrix file')
    
    global gl_args
    gl_args = parser.parse_args

    DisplayMessage('Command line processed: Successfully')

    return


#validate read function

def ValidateFileRead(theFile):
    #os path valid
    if not os.path.exists(theFile):
        raise argparse.ArgumentTypeError('File does not exist')
    
    #readable path
    if os.access(theFile, os.R_OK):
        return theFile
    else:
        raise argparse.ArgumentTypeError('File is not readable')

def DisplayMessage(msg):
    if gl_args.verbose:
        print(msg)
    return
