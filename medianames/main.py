import os 
import shutil
from utils.helper_functions import *

def scan_folder(path):
    try:
        # Ensure the path is a directory
        if os.path.isdir(path):
            #print(f"### Scanning folder: {path}")
            
            # List all files and folders in the given path
            entries = os.listdir(path)

            # Separate folders and files
            folders = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
            files = [entry for entry in entries if os.path.isfile(os.path.join(path, entry))]


            # Print folder names
            print("\nFolders:")
            for folder in folders:               
                cleaned_name = clean_folder_name(os.path.basename(folder))
                print("Cleaned folder name: ", cleaned_name)
                
                desired_path = path
                # print("At path: ", path)
                if is_season(cleaned_name):
                    desired_path = os.path.join(path, get_show(cleaned_name))
                    if (is_episode(cleaned_name)):
                        desired_path = os.path.join(desired_path, get_season(cleaned_name))

                    try:
                        os.makedirs(desired_path)
                    except Exception as e:
                        print(f"Could not create directory: {desired_path} {e}")
                    try:
                        os.makedirs(desired_path)
                    except Exception as e:
                        print(f"Could not create directory: {desired_path} {e}")
                try:
                    ugly_path = os.path.join(path, folder)
                    pretty_path = os.path.join(path, cleaned_name)
                    shutil.move(ugly_path, pretty_path)
                    shutil.move(pretty_path, desired_path)
                except Exception as e:
                    print(f"Could not move {path} -> {desired_path}: {e}") 


            # Print file names
            for file in files:
                cleaned_file = clean_folder_name(file)
                print("Cleaned file name: ", cleaned_file)
                if is_season(cleaned_file):
                    show = get_show(cleaned_file).capitalize()
                    season = get_season(cleaned_file).upper()
                    desired_path = os.path.join(path, show, season)
                    try:
                        os.makedirs(desired_path)
                    except Exception as e:
                        print(f"Could not create directory: {desired_path} {e}")
                    try:
                        shutil.move(os.path.join(path, file), desired_path)
                    except Exception as e:
                        print(f"Could not move {path} -> {desired_path}: {e}") 

                
        else:
            print(f"The path '{path}' is not a valid directory.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    scan_folder("/mnt/media/data/downloads/extracted")
    
