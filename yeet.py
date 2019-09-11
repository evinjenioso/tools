#!/usr/local/bin/python3

import os, os.path
import shutil
import pathlib

go = "y"
source = '/Users/epasqualetti/Desktop/'
screenshots = '/Users/epasqualetti/Desktop/screenshots/'
desklist = os.listdir("/Users/epasqualetti/Desktop/")

if not os.path.exists(screenshots):
                    os.mkdir(screenshots)

print(f"This will sort screenshots into dated folders under /Users/epasqualetti/Desktop/screenshots/.")
print("    ")

#print(dest)

def migrate():
    print(f"Sort screenshots?  (y/n)")
    request = input()
    if request == go:
        print(    )

# Test: Print out files to be moved
#        for file in desklist:
#            if file.startswith("Screen"):
#                test = file.split(" ")[2]
#                print(test)

# Separate files by date
        for file in desklist:
            if file.startswith("Screen"):
                dirsplit = file.split(" ")[2]
                dest = f'/Users/epasqualetti/Desktop/screenshots/{dirsplit}'
                if not os.path.exists(dest):
                    os.mkdir(dest)
                if os.path.exists(dest):
                    shutil.move(source+file,dest)
    print (f"The screenshots have been sorted into dated folders under /Users/epasqualetti/Desktop/screenshots/")

migrate()