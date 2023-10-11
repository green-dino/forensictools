import re
import sys
import os
from prettytable import PrettyTable

def analyze_large_file_for_urls(file_path, chunk_size):
    print("\nSimple File Search v2\n")

    try:
        # Verify file is real
        if os.path.isfile(file_path):
            urls_found = {}  # Dictionary to store the URLs and their occurrences
            urlPattern = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w\.?=%&=\-@/$,]*')
            with open(file_path, 'rb') as targetFile:
                while True:
                    fileChunk = targetFile.read(chunk_size)
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
            print(file_path, "is not a valid file")
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

        print("The PrettyTable has been saved as 'urls_table.html.'")

    except Exception as err:
        sys.exit("\nException: " + str(err) + " Script Aborted")

    print("\nFile Processed ... Script End")

if __name__ == "__main__":
    file_path = input("Enter the name of a large File: ")
    chunk_size = int(input("What size chunks?  "))
    analyze_large_file_for_urls(file_path, chunk_size)
