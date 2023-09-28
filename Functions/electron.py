import os
import subprocess
import csv

# Define the search directory
search_dir = '/Applications'

# Define the filename pattern
file_pattern = '*Electron Framework*'

# Define the output file path
output_file = 'electron_results.txt'

# Define the shell command to execute
command = (
    'find /Applications -type f -name "*Electron Framework*" -exec '
    'sh -c "echo  \\\"{}\\\" && strings \\\"{}\\\" | grep \'Chrome/[0-9.]* Electron/[0-9]\' | head -n1 && echo " \\;'
)

# Run the shell command
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Split the result into lines
output_lines = result.stdout.splitlines()

# Create a CSV file and write the results
with open(output_file, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write the header row
    csv_writer.writerow(["File Path", "Electron Version"])
    
    # Write the data rows
    for line in output_lines:
        # Split the line into parts based on space
        parts = line.split(' ', 1)
        
        # Check if there are at least 2 parts (file path and Electron info)
        if len(parts) >= 2:
            file_path, electron_info = parts
            # Write to CSV
            csv_writer.writerow([file_path.strip(), electron_info.strip()])
        else:
            # Handle the case where there is no Electron version information
            file_path = parts[0]
            # Write to CSV with no Electron version
            csv_writer.writerow([file_path.strip(), "No Electron Version"])

print(f"Results written to {output_file}")