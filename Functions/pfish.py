#pfish- python File System Hash program 

import logging
import time
import sys
import _pFish # support function module 

if __name__=='__main__':
    PFISH_Version='1.0'
    #turn on logging

logging.basicConfig(filename='pFishLog.log',level=logging.DEBUG, format='%(asctime)s%(message)s')   

# Post Start scan message to log 
logging.info('Welcome to p-fish v 1.0 ... New Scan Started')

# Record System Information
logging.info('System:'+sys.platform)
logging.info('Version: '+sys.version)


# Process Command Line Args 
_pFish.ParseCommandLine()

# Record Start time 
startTime = time.time()


# Traverse file systems and Hash files
filesProcessed = _pFish.WalkPath()

# Duration 
endTime = time.time()
duration = endTime - startTime

logging.info('Files Processed:' + str(filesProcessed))
logging.info('Elapsed Time: ' + str(duration)+'seconds')
logging.info('Program Termingated Normally')
