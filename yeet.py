#!/usr/local/bin/python3

import datetime
import os, os.path
import shutil, glob
import pathlib

dia = datetime.date.today()
diaday = f"{dia}"
go = "yes" or "Yes" or "Y" or "y" or "yeet"
source = '/Users/epasqualetti/Desktop/'
dest = f"/Users/epasqualetti/Desktop/screenshots/{dia}"
files = os.listdir("/Users/epasqualetti/Desktop/")

print(dest)
print(f"This gon' yeet them screenshots into {dest}.")
print(    )

def yeet():
    print(f"Yeet them screenshots into {dest} or nah? ")
    yeetin = input()
    if yeetin == go:
        os.mkdir(dest)
        for f in files:
            if f.startswith("Screen"):
                shutil.move(source+f,dest)
        print (f"Them screenshots done been yote into {diaday}.")
    else:
        print (f"Them screenshots ain't been yote.")

yeet()