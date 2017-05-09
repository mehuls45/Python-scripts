#! python3

# Practice Selective Copy
# imageFinder.py - Copies all the images from a directory and stores them into a new folder

import os
import shutil


def selectiveCopy(folder):
    num = 1
    folder = os.path.abspath(folder) # make sure folder is absoulte
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if not filename.endswith('.jpg') or filename.endswith('.JPG'):
                continue
            
            #shutil.copy(filename, 'C:\\destination_folder')  # Commented out to protect against accidental copying
            print(str(num)+'. Copying ' + filename + '...')   # Print only to verify if working correctly
            num += 1


selectiveCopy(r'source_path')
print('Done')
