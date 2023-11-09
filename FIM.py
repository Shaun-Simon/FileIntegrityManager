import os # pathing to files
import hashlib # hashing calculations
import time # while loop sleep

BASE_PATH = r'C:\Users' #FIM main directory, where new baselines will be created
FILES_PATH = r'C:\Users' #FIM files to be monitored
BASELINE_FILE_PATH = os.path.join(BASE_PATH, 'baseline.txt') #FIM Baseline Locator

def calculate_file_hash(filepath):
    hasher = hashlib.sha512()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def erase_baseline_if_already_exists(): # deletes the existsing baseline 
    if os.path.exists(BASELINE_FILE_PATH):
        os.remove(BASELINE_FILE_PATH)

print("\nWhat would you like to do?\n")
print("    A) Collect new Baseline?")
print("    B) Begin monitoring files with saved Baseline?")
response = input("\nPlease enter 'A' or 'B': ").upper()
print()

if response == "A":
    erase_baseline_if_already_exists()

    #collecting all files to be monitored
    files = os.listdir(FILES_PATH)

    # calculates each files hash value and adds it to the baseline
    with open(BASELINE_FILE_PATH, 'a') as baseline_file:
        for f in files:
            file_path = os.path.join(FILES_PATH, f)
            file_hash = calculate_file_hash(file_path)
            baseline_file.write(f"{file_path}|{file_hash}\n")

elif response == "B":
    file_hash_dictionary = {}

    # loads file|hash from baseline file and store them in a dictionary
    with open(BASELINE_FILE_PATH, 'r') as baseline_file:
        for line in baseline_file:
            file_path, file_hash = line.strip().split("|")
            file_hash_dictionary[file_path] = file_hash

    #continous monitoring of selected path files and compares hash values with saved baseline
    while True:
        time.sleep(2)

        files = os.listdir(FILES_PATH)

        # calculating the new hash value of each file to compare to saved baseline
        for f in files:
            file_path = os.path.join(FILES_PATH, f)
            file_hash = calculate_file_hash(file_path)

            # notify if a new file being created in the monitored path
            if file_path not in file_hash_dictionary:
                print(f"{file_path} has been created!")

            else:
                # notify if a new file has been changed
                if file_hash_dictionary[file_path] == file_hash:
                    # passes through if the file hasn't changed
                    pass
                else:
                    # notify that the file has been changed 
                    print(f"{file_path} has changed!")

        for key in list(file_hash_dictionary.keys()):
            baseline_file_still_exists = os.path.exists(key)
            if not baseline_file_still_exists:
                # baseline comparison to detect if a file has been deleted
                print(f"{key} has been deleted!")
