# Python Text Processing Scripts

Forensic toolset that examines File Structures, File Integrity and Examine documents, word counts and pattern analysis. 



## _psearch

### Overview

The `_psearch` Python script is designed for conducting keyword searches within a target file using a weighted matrix approach. It allows users to specify the keyword file, target file, and weight matrix file as command-line arguments. When a keyword match is found in the target file, the script displays a buffer of values around the match, providing context for the match.

### Usage

To use `_psearch`, follow these steps:

1. Command Line: Run the script from the command line, providing the necessary command-line arguments:


- `-k` or `--keywords`: Specify the keyword file.
- `-t` or `--target`: Specify the target file.
- `-w` or `--weights`: Specify the weight matrix file.

2. The script will perform the keyword search and display results with context.

### Development Notes

- This script can be further customized to include advanced features or different search algorithms.
- Logging messages can be adapted to fit your preferred logging method.
- Contributions to the script are welcome.

## _pfish

### Overview

The `_pfish` Python script is designed for calculating hash values of files in a specified directory using different hashing algorithms (MD5, SHA256, or SHA512). It generates a CSV report containing file details, including name, path, size, and hash values. The script is intended for use in a command-line environment.

### Usage

To use `_pfish`, follow these steps:

1. Command Line: Run the script from the command line, providing the necessary command-line arguments:


- `--md5`, `--sha256`, `--sha512`: Specify the hashing algorithm to use (choose one).
- `-d` or `--rootPath`: Specify the root directory path for hashing.
- `-r` or `--reportPath`: Specify the directory where the CSV report will be saved.

2. The script will calculate hash values for all files within the specified directory using the selected hashing algorithm and generate a CSV report.

### Development Notes

- This script supports hashing using MD5, SHA256, or SHA512 algorithms.
- Validation functions ensure that the specified directories exist, are readable, and writable.
- The script provides verbose mode for additional progress messages.
- Contributions to the script are welcome.

## _searchWords

### Overview

The `_searchWords` Python script is designed for searching through a text file for specific words and performing word frequency analysis. It allows users to load a list of search words from a file, search for words within another text file, and analyze the frequency of words found. The script is intended for use in a command-line environment.

### Usage

To use `_searchWords`, follow these steps:

1. Prepare a Word List File: Create a text file containing a list of words you want to search for, with each word on a separate line.

2. Run the Script:


- `--md5`, `--sha256`, `--sha512`: Specify the hashing algorithm to use (choose one).
- `-d` or `--rootPath`: Specify the root directory path for hashing.
- `-r` or `--reportPath`: Specify the directory where the CSV report will be saved.

2. The script will calculate hash values for all files within the specified directory using the selected hashing algorithm and generate a CSV report.

### Development Notes

- This script supports hashing using MD5, SHA256, or SHA512 algorithms.
- Validation functions ensure that the specified directories exist, are readable, and writable.
- The script provides verbose mode for additional progress messages.
- Contributions to the script are welcome.

## _searchWords

### Overview

The `_searchWords` Python script is designed for searching through a text file for specific words and performing word frequency analysis. It allows users to load a list of search words from a file, search for words within another text file, and analyze the frequency of words found. The script is intended for use in a command-line environment.

### Usage

To use `_searchWords`, follow these steps:

1. Prepare a Word List File: Create a text file containing a list of words you want to search for, with each word on a separate line.

2. Run the Script:


3. Input File: Enter the file path and name of the text file you want to search through.

4. Search Words: The script will load the list of search words from the previously created file.

5. Search Type: Choose between an exact or partial search.

- Exact: Searches for an exact match of the entered word.
- Partial: Searches for words containing the entered word as a substring.

6. Enter Word: Enter the word you want to search for in the selected search type.

7. Search Results: The script will display whether the word was found or not found based on the search type.

8. Word Frequency Analysis: After the search, the script will perform a word frequency analysis on the loaded search words and display the count of each word.

9. Repeat: You can choose to search again or exit the script.

### Development Notes

- This script can be customized for specific use cases and extended to include more advanced features.
- Error handling for file operations is included to handle missing or inaccessible files.
- Contributions to the script are welcome.

## Disclaimer

These scripts are provided as-is and may require additional testing and modification to suit your specific use cases. Ensure that you have the necessary permissions to access the specified directories and files.

Feel free to contribute to the development of these scripts, adapt them to your needs, and make improvements as necessary.

