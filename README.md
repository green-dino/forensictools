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