import os

GetFiles = os.walk(os.getcwd())
FilesInDirectory = []
for walk_output in GetFiles:
    for file_name in walk_output[-1]:
        FilesInDirectory.append(file_name)

for file_ext in FilesInDirectory:
    print(os.path.splitext(file_ext)[1])
    