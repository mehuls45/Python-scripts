#! pyhton3
# Walks through a directory tree searching for files > 1 GB
# and displays the filename along with size in GBs

import os

def fileSize(folder):
    num = 1
    folder = os.path.abspath(folder) # make sure folder is absolute

    for foldername,subfolders, filenames in os.walk(folder):

        for filename in filenames:

            s = os.path.getsize(foldername+ '\\' + filename)

            if int(s) > 1000000000:
                s = s/1000000000
                print(str(num)+'. '+filename+'  '+str(s))
                num += 1


#fileSize('C:\\')
fileSize('C:\\Users\\mehul\\Desktop\\Mehul\\')
print('Done')
