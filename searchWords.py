import sys

searchWords = set()

try:
    file_path = input('Enter the file path and name you want to search through: ')
    with open(file_path) as fileWords:
        for line in fileWords:
            searchWords.add(line.strip())
except FileNotFoundError:
    print(f'The file {file_path} does not exist. Please create the file or add words to it.')
    sys.exit()
except Exception as e:
    print('File Handling Error:', str(e))
    sys.exit()

print(searchWords)

word_to_search = input('Enter a word to search: ')

if word_to_search in searchWords:
    print('Found Word')
else:
    print('Not found')
