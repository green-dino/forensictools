import sys
import string

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

def word_frequency_analysis(search_words):
    word_count = {}
    for word in search_words:
        # Remove punctuation and convert to lowercase for consistency
        cleaned_word = word.translate(str.maketrans('', '', string.punctuation)).lower()
        if cleaned_word in word_count:
            word_count[cleaned_word] += 1
        else:
            word_count[cleaned_word] = 1
    return word_count

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

    # Perform Word Frequency Analysis
    word_count = word_frequency_analysis(searchWords)
    print('Word Frequency Analysis:')
    for word, count in word_count.items():
        print(f'{word}: {count}')

    again = input('Do you want to search again? (yes/no): ')
    if again.lower() != 'yes':
        break
