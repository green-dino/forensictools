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

# Search Words, use command line arguments, searches target for keywords



def SearchWords():
    #empty set of search words
    searchWords=set()
    try:
        fileWords = open (gl_args.keyWords)
        for line in fileWords:
            searchWords(line.strip())
    except:
        log.error('Keyword file failure:'+gl_args.keyWords)
        sys.exit()
    finally:
        fileWords.close()
    # log entry words to search for
    log.info('Search Words')
    log.info('Input File:'+gl_args.keyWords)
    log.info(SearchWords)

    # open and read the target file, load bytearray

    try:
        targetFile = open (gl_args.srchTarget, 'rb')
        baTarget = bytearray(targetFile.read())
    except:
        log.error('Target File Failure:'+ gl_args.srchTarget)
        sys.exit()
    finally:
        targetFile.close()
    # post to log

    log.info('Target of Search:'+gl_args.srchTarget)
    log.info('File Size:'+ str(sizeOfTarget))

    baTargetCopy = class_Matrix()

    #search loop
    #replace non characters with zero

    for i in range(0, sizeOfTarget):
        character = chr(baTarget[i])
        if not character.isalpha():
            baTarget[i] = 0
    
    # extract possible words from bytearray, inspect searchword list, 
    #create empty list of probable not found items

    indexOfWords = []
    cnt = 0
    for i in range(0, sizeOfTarget):
        character = chr(baTarget[i])
        if character.isalpha():
            cnt+=1
        else:
            if (cnt >=MIN_WORD and cnt <= MAX_WORD):
                newWord = ""
                for z in range(i-cnt,i):
                    newWord = newWord + chr(baTarget[z])
                newWord = newWord.lower()
                if (newWord in searchWords):
                        PrintBuffer(newWord, i-cnt, baTargetCopy, i PREDECESSOR_SIZE, WINDOW_SIZE) 
                        print
            else:
                notFound.append(newWord)
                cnt=0
            else:
                cnt = 0
            
