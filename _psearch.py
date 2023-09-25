# psearch support functions 

import argparse
import os
import logging
import sys

log = logging.getLogger('main._psearch')


#constants
MIN_WORD = 5 # min word size in bytes
MAX_WORD = 15 # max word size in bytes
PREDECESSOR_SIZE = 32 # values to print before match found
WINDOW_SIZE = 128  # values to dump when match 


# parse command function, uses argparse 

def ParseCommandLine():
    parser = argparse.ArgumentParser('Python Search')

    parser.add_argument('-v', '--verbose', help='enables the printing of additional program messages', action='store_true')
    parser.add_argument('-k', '--keyWords', type=ValidateFileRead,
                        required=True,help='Specify the file containing search words')
    parser.add_argument('-t','--srchTarget', type=ValidateFileRead,
                        required=True, help="specifiy the target file to search")
    parser.add_argument('-m','--theMatrix', type=ValidateFileRead,
                        required=True, help='Specify the weight matrix file')
    
    global gl_args
    gl_args = parser.parse_args()

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
    log.info(searchWords)
       # Calculate the size of the target file
    sizeOfTarget = len(baTarget)

    baTargetCopy = class_Matrix

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
                        PrintBuffer(newWord, i-cnt, baTargetCopy, i- PREDECESSOR_SIZE, WINDOW_SIZE) 
                        indexOfWords.append([newWord, i-cnt])
                        cnt = 0
                        print
                else:
                    cnt = 0
    PrintAllWordsFound(indexOfWords)
    return
# hexidecimal / ASCII Page 

def  PrintHeading():
    print("offset 00 01 02 03 04 05 06 070 80 09 0A 0B 0C 0D 0E 0F ASCII")
    print("--------------------------------------------------------------")
    return

def PrintBuffer(word, direcOffset, buff, offset, hexSize):
    print("%08X  " % (direcOffset))
    PrintHeading()
    for i in range(0, 16):
        if i == 0:
            print("%08x" % i, end=' ')
        else:
            byteValue = buff[i + offset]
            print("%02x" % byteValue, end=' ')
    print("")
    for j in range (0,16):
        byteValue = buff[i+j]
        if (byteValue >=0x20 and byteValue <=0x7f):
            print("%c"%byteValue, end='')
        else:
            print('.', end=''),
    print('')
    return


def PrintAllWordsFound(wordList):
    print ("Index of all words")
    print("----------------------------")

    wordList.sort()

    for entry in wordList:
        print (entry)
    print ('---------------')
    print

    return

class class_Matrix:
    weightedMatrix = set()
    def __init__(self):
        try:
            fileTheMatrix = open(gl_args.theMatrix, 'rb')
            for line in fileTheMatrix:  # Added ':' to the for loop
                value = line.strip()
                self.weightedMatrix.add(int(value, 16))
        except:
            log.error('Matrix File Error' + gl_args.theMatrix)
            sys.exit()
        finally:
            fileTheMatrix.close()