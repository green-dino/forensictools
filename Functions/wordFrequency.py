import os
import re
from prettytable import PrettyTable

print("Current working directory:", os.getcwd())

from pathlib import Path

file_path = Path('dialog.txt')
if file_path.is_file():
    with file_path.open('r') as file:
        fileContents = file.read()
else:
    print("File not found or path is incorrect.")

# Convert the variable fileContents into all lowercase
fileContents = fileContents.lower()
# Remove all punctiuation and whatnot to focus only on words
cleanContent = re.sub(r'[^A-Za-z0-9 ]+', '', fileContents)

# Read in the contents of the stopWords.txt file into the variable: STOP_WORDS
file_path = Path('stop_Words.txt')
if file_path.is_file():
    with file_path.open('r') as file:
        STOP_WORDS = file.read().split()
        
sampleSentence = input("Enter a sample sentence: ")

# Split the sample sentence into a list of words
wordList = cleanContent.split()

# Create a dictionary named wordDict
wordDict = {}

for eachWord in wordList:
    # Skip words found in the STOP_WORDS list or words that are less than 4 or greater than 12 characters
    if eachWord in STOP_WORDS or len(eachWord) < 4 or len(eachWord) > 12:
        continue
    
    # If the word is not in the dictionary, add it with a count of 1
    if eachWord not in wordDict:
        wordDict[eachWord] = 1
    else:
        # If the word is already in the dictionary, increment its count
        wordDict[eachWord] += 1

# Create a pretty table named wordTable
wordTable = PrettyTable()
wordTable.field_names = ["WORD", "OCCURS"]

wordSort = sorted(wordDict.items(), key=lambda x:x[1])

wordSort.reverse()

# Add entries from wordDict to the table
for word, count in wordSort:
    wordTable.add_row([word, count])

print("Word Frequency Table:")

print(wordTable)



# Output the contents of the wordTable to a file
output_filename = "Output_file.txt"
with open(output_filename, 'w') as output_file:
    output_file.write(str(wordTable))
    
print(f"Word Frequency Table saved to '{output_filename}'.")