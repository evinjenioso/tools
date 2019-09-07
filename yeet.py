#!/usr/local/bin/python3

import datetime
import os, os.path
import shutil, glob
import pathlib

dia = datetime.date.today()
diaday = f"{dia}"
label = f"Screenshot {dia}"
go = "yes" or "Yes" or "Y" or "y"

source = '/Users/epasqualetti/Desktop/'
path = '/Users/epasqualetti/Desktop/screenshots/'
dest = path+diaday
files = os.listdir("/Users/epasqualetti/Desktop/")

print(dest)
print(f"This gon' yeet them screenshots into {dest}.")
print(    )

def yeet():
    print(f"Yeet them screenshots into {dest} or nah? ")
    yeetin = input()
    if yeetin == go:
        os.mkdir(diaday)
        for f in files:
#            if f.startswith("Screen"):
            if f.startswith(f"Screenshot {diaday}"):
                shutil.move(source+f,dest)
        print (f"Them screenshots done been yote into {diaday}.")
    else:
        print (f"Them screenshots ain't been yote.")

yeet()
#print(diaday)
#if __name__ == '__main__':
#curdir = os.getcwd()
#print(curdir)



