import os
from pathlib import Path
# Path in which we have to count files and derectories
PATH = '/Users/' #Give the path name here 
fileCount = 0 
dirCount = 0 
for root, dirs, files in os.walk(PATH):
    print ('Looking in:',root)
    for directories in dirs:
        dirCount += 1 
    for Files in files:
        fileCount += 1

#clcodind.com
print ('Number of files',fileCount)
print ('Number of Directories',dirCount)
print ('Total:', (dirCount+fileCount))