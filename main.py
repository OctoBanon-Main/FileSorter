import os
import json

DirectoryNames = ['Audio', 'Videos', 'Photos', 'Icons', 'Archives', 'Other', 'Executable', 'Disk Images']

skip_executables = False
asked_for_skip = False

files = {}

for dir in DirectoryNames:
    try:
        os.mkdir(dir)
    except OSError:
        os.mkdir(dir + "_moved")

with open("config.json", "r") as read_file:
    files = json.load(read_file)

GetFiles = os.walk(os.getcwd())
FilesInDirectory = []
for walk_output in GetFiles:
    for file_name in walk_output[-1]:
        FilesInDirectory.append(file_name)

for filename in FilesInDirectory:
    if os.path.basename(__file__) != filename:
        extension = os.path.splitext(filename)[1]
        try:
            if files[extension] == "Executable" and skip_executables == True and asked_for_skip == True:
                continue
            elif files[extension] == "Executable" and skip_executables == False and asked_for_skip == True:
                os.rename(filename, files[extension] + "/" + filename)
            else:
                asked_for_skip = True
                choice = input("WARNING! Found executable file or its component:" + filename + ". Moving these files can broke executables proper work. Do you want to move executables/components? Y/N: ")
                if choice in {'y', 'Y'}:
                    os.rename(filename, files[extension] + "/" + filename)
                    continue
                elif choice in {'n', 'N'}:
                    skip_executables = True
                    continue
            os.rename(filename, files[extension] + "/" + filename)
        except:
            print(filename + ": failed")
