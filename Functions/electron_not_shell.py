import os
import re
from packaging import version
import csv

safe_versions = [version.parse(ver) for ver in ['22.3.24', '24.8.3', '25.8.1', '26.2.1']]
pattern = re.compile(r'Chrome/[0-9.]+ Electron/([0-9.]+)')

results = []

def check_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        match = pattern.search(content)
        if match:
            electron_version = version.parse(match.group(1))
            safe_versions_sorted = sorted(safe_versions, key=lambda v: v.numify(), reverse=True)
            if electron_version < safe_versions_sorted[0]:
                results.append((file_path, electron_version))

def find_electron_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".js"):
                file_path = os.path.join(root, file)
                check_file(file_path)

if __name__ == "__main__":
    directory = "/Applications"
    find_electron_files(directory)

    # Write results to a CSV file
    with open('vulnerable_electron.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['File Path', 'Vulnerable Electron Version'])
        csv_writer.writerows(results)
