import os
import subprocess

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

# Print the result
if result.returncode == 0:
    print(result.stdout.strip())
else:
    print(f"Error executing command: {result.stderr.strip()}")

# Open the output file for writing
with open(output_file, 'w') as f:
    # Walk through the directory and search for matching files
    for root, _, files in os.walk(search_dir):
        for filename in files:
            if file_pattern in filename:
                file_path = os.path.join(root, filename)

                # Execute the shell command
                command = command_template.format(file_path, file_path)

                # Debug output
                print(f"Processing file: {file_path}")

                result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

                # Write the result to the output file
                if result.returncode == 0:
                    output = result.stdout.strip()
                    f.write(output + '\n')
                    print(output)
                else:
                    error_message = f"Error executing command for {file_path}: {result.stderr.strip()}"
                    f.write(error_message + '\n')
                    print(error_message)

print(f"Results saved to {output_file}")
