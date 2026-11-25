import os
import argparse

def parseArgs():

    args = argparse.ArgumentParser()
    args.add_argument("--path", default=".")
    return args.parse_args()

def countFiles(dirpath):

    count = {}

    for i in os.listdir(dirpath):
        full = os.path.join(dirpath, i)

        if os.path.isdir(full):
            count["dir"] = count.get("dir", 0) + 1

        else:
            ext = os.path.splitext(i)[1]
            count[ext] = count.get(ext, 0) + 1

    return count

def bigFileSize(dirpath):
    fileSize = 0
    x = os.listdir(dirpath)
    li = []
    for folder, subfolders, files in os.walk(dirpath):
        '''
        full = os.path.join(dirpath, i)
        if os.path.isfile(full):    
            fileSize = os.path.getsize(full)
            li.append((fileSize, i))

    y = sorted(li, reverse=True)
    result = y[:10]
    for l in result:
        print(*l)
    '''
        print(f"\nFolders {folder}\nSubfolder {subfolders}\nFiles {files}")

args = parseArgs()
count = countFiles(args.path)
print(count)
bigFileSize(args.path)