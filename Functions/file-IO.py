'''
Simple File I/O
Read a text file and display the contents

Script requires the file test.txt to be in the
same folder as the script
'''
try:

    with open("test.txt",'r') as book:
        content = book.read()
        print(content)

except Exception as err:
    print("Exception: ", str(err))
    