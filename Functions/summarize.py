import re
import sys
import os
from prettytable import PrettyTable

#This script is particularly useful for analyzing and summarizing the distribution of URLs within large text files. It can be helpful for web scraping, log analysis, or any task involving URL identification.
#The script efficiently processes large files by reading them in smaller chunks, reducing memory usage.
#Users can further customize the regular expression pattern for URL identification to match their specific use case.
#The generated PrettyTable can be saved as an HTML file, making it easy to share and view the results in a web browser.

print("\nSimple File Search v2\n")

try:
    # Prompt user for a file and Chunk Size
    largeFile = input("Enter the name of a large File: ")
    chunkSize = int(input("What size chunks?  "))

    # Regular expression to find URLs in the file
    urlPattern = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w\.?=%&=\-@/$,]*')

    if os.path.isfile(largeFile):  # Verify file is real
        urls_found = {}  # Dictionary to store the URLs and their occurrences
        with open(largeFile, 'rb') as targetFile:
            while True:
                fileChunk = targetFile.read(chunkSize)
                fileChunk = fileChunk.lower()  # broaden search

                if fileChunk:  # if we still have data
                    # Search this chunk for URLs
                    urls = urlPattern.findall(fileChunk)
                    for url in urls:
                        url = url.decode('utf-8')  # Convert bytes to string
                        if url in urls_found:
                            urls_found[url] += 1
                        else:
                            urls_found[url] = 1

                else:
                    # File has been processed
                    break
    else:
        print(largeFile, "is not a valid file")
        sys.exit("Script Aborted")

    # Create a PrettyTable to display the results
    table = PrettyTable()
    table.field_names = ["URL", "Occurrences"]
    for url, occurrences in urls_found.items():
        table.add_row([url, occurrences])

    print(table)
    # Save the PrettyTable as an HTML file
    with open("urls_table.html", "w") as html_file:
        html_file.write(table.get_html_string())

    print("The PrettyTable has been saved as 'urls_table.html'.")


except Exception as err:
    sys.exit("\nException: " + str(err) + " Script Aborted")

print("\nFile Processed ... Script End")
