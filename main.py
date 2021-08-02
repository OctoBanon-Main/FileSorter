import os
import magic

GetFiles = os.walk(os.getcwd())
FilesInDirectory = []

def DetermineExtension(filename):
    return magic.from_file(filename)

for walk_output in GetFiles:
    for file_name in walk_output[-1]:
        FilesInDirectory.append(file_name)

for file_ext in FilesInDirectory:
    print(os.path.splitext(file_ext)[1])
    #extension = os.path.splitext(file_ext)[1]
    #print(file_ext + " - " + DetermineExtension(file_ext))
    
