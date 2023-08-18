import os
import sys

EXTENSION = ".txt"
num = 1

def serialise_files(path, num):
    cwd = os.getcwd()
    os.chdir(path)
    
    for root, dirs, files in os.walk(path):
        for file in files: # modify first level of files
            if file.endswith(EXTENSION):
                os.rename(file, str(num) + EXTENSION)
                num += 1

    os.chdir(cwd)

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        raise Exception("You must pass a target directory - only.")
    
    target = args[1]
    serialise_files(target, num)
