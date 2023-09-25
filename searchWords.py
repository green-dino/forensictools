import sys

def load_search_words(file_path):
    search_words = set()
    try:
        with open(file_path) as fileWords:
            for line in fileWords:
                search_words.add(line.strip())
    except FileNotFoundError:
        print(f'The file {file_path} does not exist. Please create the file or add words to it.')
    except Exception as e:
        print('File Handling Error:', str(e))
    return search_words

while True:
    file_path = input('Enter the file path and name you want to search through: ')
    searchWords = load_search_words(file_path)

    if not searchWords:
        continue

    print(searchWords)

    word_to_search = input('Enter a word to search: ')

    if word_to_search.lower() in (word.lower() for word in searchWords):
        print('Found Word')
    else:
        print('Not found')

    again = input('Do you want to search again? (yes/no): ')
    if again.lower() != 'yes':
        break
