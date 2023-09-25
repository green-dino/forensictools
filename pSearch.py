# Python word searcher 

import logging 
import time
import _psearch

if __name__ == '_main_':
    Version = '1.0'
    logging.basicConfig(filename='pSearchLog.log', level=logging.DEBUG, format='%(asctime)s%(messages)s')

# proccess command line args
_psearch.ParseCommandLine()

log = logging.getLogger('main._psearch')
log.info("p-search started")

# record start time
startTime = time.time()

# perform keyword search
_psearch.SearchWords()

# record Ending time

endTime = time.time()
duration = endTime - startTime

logging.info('Elapsed Time: '+ str(duration)+ 'seconds')
logging.info('')
logging.info('Program Terminated Normally')


