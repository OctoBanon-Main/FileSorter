import os
import json

DirectoryNames = ['Audio','Videos','Photos','Archives','Other']

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
            os.rename(filename, files[extension] + "/" + filename)
        except:
            print(filename + ": failed")
