import os


files_to_check = [
    "Downloads/Dr_Shashi_Tharoor.jpg",
    "Downloads/Plaksha_Faculty.jpg",
    "Downloads/Lab 5-Spring 2025.ipynb",
    "distance_classification.py"
]

all_files_exist = True

for file in files_to_check:
    if os.path.exists(file):
        print(f"{file} found.")
    else:
        print(f"{file} is missing!")
        all_files_exist = False

if all_files_exist:
    print("All files are present.")
else:
    print("Some files are missing. Please check!")


