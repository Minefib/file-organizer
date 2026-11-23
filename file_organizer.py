import os
import argparse

def parseArgs():
    args = argparse.ArgumentParser()
    args.add_argument("--path", default=".")
    return args.parse_args()

args = parseArgs()
count = {}
x = os.listdir(args.path)

for i in x:
    full = os.path.join(args.path, i)
    if os.path.isdir(full):
        count["dir"] = count.get("dir", 0) + 1
    else:
        ext = os.path.splitext(i)[1]
        count[ext] = count.get(ext, 0) + 1
print(f"{count}")

