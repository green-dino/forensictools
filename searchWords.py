import sys
searchWords = set()
try:
    fileWords = open('bike.txt')
    for line in fileWords:
        searchWords.add(line.strip())
except:
    print('File Handling Error')
    sys.exit()
print(searchWords)
if ('Touring' in searchWords):
    print('Found Word')
else:
    print('not found')
    