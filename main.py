import os
import json

textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))
DirectoryNames = ['Music','Videos','Photos','Archives','Other','Binary']

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
            if is_binary_string(open(filename, 'rb').read(1024)):
                os.rename(filename, "Binary/" + filename)
            else:
                os.rename(filename, files[extension] + "/" + filename)
        except:
            print(filename + ": failed")
