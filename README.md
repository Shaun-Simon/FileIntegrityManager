<h1>File Integrity Monitor</h1>

<h2>Description</h2>
This is a simple, proof of concept File Integrity Monitor.  a Python script that monitors files in a specified folder for changes and alerts the user if any files are created, modified, or deleted. It uses file hashes to detect alterations and provides a baseline for comparison.

## Usage
- Option A: Collect New Baseline

If you choose option A, the script will delete the existing baseline file (if it exists) and create a new one by calculating hashes for all files in the specified folder.

-  Option B: Begin Monitoring With A Previosuly Saved Baseline

If you choose option B, the script will load the baseline file and start continuously monitoring the specified folder. It will alert you if a new file is created, if a file is modified, or if a baseline file is deleted.

## Configuration
- BASE_PATH: The base path for the FIM baseline save location
- FILES_PATH: The path to the folder containing files to be monitored
- BASELINE_FILE_PATH: The path to the baseline file
