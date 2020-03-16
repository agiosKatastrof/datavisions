#!/usr/bin/env python

import re
import os
from os import listdir
from os.path import isfile, join

mypath = '/home/joe/temp'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for f in files:
    match = re.match(r"\d{8}",f)
    yr = match[0][0:4]
    mo = match[0][4:6]
    dy = match[0][6:8]
    newfname = yr + "-" + mo + "-" + dy + ".pdf"
    ffile = mypath + "/" + f
    fnewfname = mypath + "/" + newfname
    print(ffile)
    print(fnewfname)
    os.rename(ffile,fnewfname)
