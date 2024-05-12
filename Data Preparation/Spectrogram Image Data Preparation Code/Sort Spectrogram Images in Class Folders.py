import os
import shutil
import glob

def create_folders(folder_path):
    labels = {
        'bass': 0,
        'brass': 1,
        'flute': 2,
        'guitar': 3,
        'keyboard': 4,
        'mallet': 5,
        'organ': 6,
        'reed': 7,
        'string': 8,
        'synth_lead': 9,
        'vocal': 10
    }

    for label in labels.values():
        os.makedirs(os.path.join(folder_path, str(label)), exist_ok=True)

def organize_files(folder_path):
    labels = {
        'bass': 0,
        'brass': 1,
        'flute': 2,
        'guitar': 3,
        'keyboard': 4,
        'mallet': 5,
        'organ': 6,
        'reed': 7,
        'string': 8,
        'synth_lead': 9,
        'vocal': 10
    }

    files = glob.glob(os.path.join(folder_path, '*.png'))

    for file in files:
        filename = os.path.basename(file)
        for label, folder_index in labels.items():
            if label in filename:
                dest_folder = os.path.join(folder_path, str(folder_index))
                shutil.move(file, dest_folder)
                break

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder of PNG files: ")
    
    create_folders(folder_path)
    organize_files(folder_path)

    print("Files have been organized successfully.")