

# forensictools
Python Tools for system analysis 

Naming conventions:
Constants 
Rule: Uppercase with underscore separation Example: HIGH_TEMPERATURE 

Local variable name 
Rule: Lowercase with bumpy caps (underscores are optional) Example: currentTemperature 

Global variable name 
Rule: Prefix gl lowercase with bumpy caps (underscores are optional) Note: Globals should be contained to a single moduleExample: gl_maximumRecordedTemperature 

Functions name 
Rule: Uppercase with bumpy caps (underscores optional) with active voice Example: ConvertFarenheitToCentigrade(. . .) 

Object name 
Rule: Prefix ob_ lowercase with bumpy caps Example: ob_myTempRecorder 

Module 
Rule: An underscore followed by lowercase with bumpy caps Example: _tempRecorder 


Use the pfish tool which references _pfish.py 

Command to get started 

python pfish.py --hash -d (directory you want to hash) -r (directory to write your results)

_psearch 
This Python script is designed for conducting keyword searches within a target file using a weighted matrix approach. It allows users to specify the keyword file, target file, and weight matrix file as command-line arguments. When a keyword match is found in the target file, the script displays a buffer of values around the match, providing context for the match.

_pfish
Overview:

This Python script is designed for calculating hash values of files in a specified directory using different hashing algorithms (MD5, SHA256, or SHA512). It generates a CSV report containing file details, including name, path, size, and hash values. The script is intended for use in a command-line environment.

Usage:

To use this script, follow these steps:

Command Line: Run the script from the command line, providing the necessary command-line arguments:
css
Copy code
python your_script.py --md5|--sha256|--sha512 -d path_to_directory -r path_to_report_directory
--md5, --sha256, --sha512: Specify the hashing algorithm to use (choose one).
-d or --rootPath: Specify the root directory path for hashing.
-r or --reportPath: Specify the directory where the CSV report will be saved.
Verbose Mode: You can enable verbose mode by including the -v or --verbose flag to print additional progress messages.
Hash Calculation: The script will calculate hash values for all files within the specified directory using the selected hashing algorithm.
CSV Report: A CSV report will be generated containing file details, including name, path, size, and hash values. The report will be saved in the specified report directory.
Functionality:

The script supports hashing using MD5, SHA256, or SHA512 algorithms.
It calculates hash values for all files in the specified directory and its subdirectories.
Validation functions ensure that the specified directories exist, are readable, and writable.
The script provides verbose mode to display progress messages.
Hash values and file details are recorded in a CSV report for further analysis.
Development Notes:

The script may require further customization or modification to meet specific requirements.
Logging messages can be adjusted to fit your preferred logging method.
Contributions:

Contributions or improvements to the script are welcome. Feel free to adapt it to your needs and contribute to its development.

Disclaimer:

This script is provided as-is and may require additional testing and modification to suit your specific use cases. Ensure that you have the necessary permissions to access the specified directories and files.


_searchWords
This Python script is designed for searching through a text file for specific words and performing word frequency analysis. It allows users to load a list of search words from a file, search for words within another text file, and analyze the frequency of words found. The script is intended for use in a command-line environment.

Usage:

To use this script, follow these steps:

Word List File: Create a text file containing a list of words you want to search for. Each word should be on a separate line.
Run the Script: Run the script from the command line or your preferred Python environment:
Copy code
python your_script.py
Input File: Enter the file path and name of the text file you want to search through.
Search Words: The script will load the list of search words from the previously created file.
Search Type: Choose whether you want to perform an exact or partial search.
Exact: Searches for an exact match of the entered word.
Partial: Searches for words containing the entered word as a substring.
Enter Word: Enter the word you want to search for in the selected search type.
Search Results: The script will display whether the word was found or not found based on the search type.
Word Frequency Analysis: After the search, the script will perform a word frequency analysis on the loaded search words and display the count of each word.
Repeat: You can choose to search again by typing "yes" or exit the script by typing "no."
Functionality:

The script loads search words from a user-specified file.
It allows users to search for words within another text file.
Users can choose between exact and partial search types.
Word frequency analysis is performed, showing the count of each word in the search list.
The script can be used iteratively to perform multiple searches.
Development Notes:

This script can be customized for specific use cases and extended to include more advanced features.
Error handling for file operations is included to handle missing or inaccessible files.
Contributions:

Contributions or improvements to the script are welcome. Feel free to adapt it to your needs and contribute to its development.

Disclaimer:

This script is provided as-is and may require additional testing and modification to suit your specific use cases. Ensure that you have the necessary permissions to access the specified directories and files.
