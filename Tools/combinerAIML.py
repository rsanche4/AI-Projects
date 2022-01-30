import fnmatch
import os

def masterWriter(fileName, masterFileName):
       
    file = open(fileName, 'r')
    master_file = open(masterFileName, 'a')
    lines = file.readlines()

    for line in lines:
        master_file.write(line)

    file.close()


for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.aiml'):
        masterWriter(file, 'MASTER_AIML.aiml')

print("SUCCESS: All files combined in MASTER_AIML.aiml")
