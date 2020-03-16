import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dill
import re
import sys
import csv
import subprocess
import string
from os import listdir
from os.path import isfile, join

def findFilesToProcess(mypath,filelist):
# find pdfs in path
# if the file has not been processed, process it

    # list of files in dir
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    dfFiles = pd.DataFrame(files, columns = ['file'])
    
    # create df of done files
    doneFiles = open(filelist).read().splitlines()
    dfDone = pd.DataFrame(doneFiles, columns = ['file'])
    
    return dfFiles[dfFiles['file'].isin(dfDone['file']) == False]

def parsePdf(f):
   cmd = ['pdf2txt.py','-S','-t','text',f]
   process = subprocess.run(cmd, capture_output=True)
   if (process.stderr):
       out = process.stderr
       print(out)
   else:
       out = processOutput(process.stdout)
   return out

def processOutput(output):
    outlist = output.splitlines()
    print("found ", len(outlist), " rows")
    i = 0
    date = None
    china = None

    for l in outlist: 
        l = str(l)

        # find the date 
        if (date is None):
            date = findDate(l)
            if (date is not None):
                print(date)
            
        # find China 
        if (china is None):
            china = findChina(l,outlist[i+1])
            if (china is not None):
                print(china)
    
        i += 1
    return 

def findChina(l,m):  
    returnChina = None
    print("looking for china")
    pattern = r'China'

    china = re.search(pattern,l)
    if(china):
        pattern = r'\d+\s*\d+\s+confirmed\s+'
        m = str(m)
        chinaNum = re.search(pattern,m)
        if(chinaNum):
            returnChina = chinaNum.group()
            pattern = r'(confirmed|\s+)'
            p = re.compile(pattern)
            returnChina = p.sub('',returnChina)
            returnChina.strip()
            print("found china", returnChina)

    return returnChina

def findDate(l):
    returnDate = None
    print("looking for the date")
    pattern = r'CET\s+\d+\s+\D+\s+2020'

    date = re.search(pattern,l)
    if(date):
        returnDate = date.group()
        returnDate = returnDate[3:]
        returnDate = returnDate.strip()
        print("found the date ", returnDate)

    return returnDate

def processFile(mypath,filelist,summary,f,runmode):
    date, ext = f.split('.')
    ffile = '/'.join([mypath,f])

    try:
        fl = open(filelist,"a+")
    except OSError:
        print("could not open filelist to append ", filelist)
        sys.exit()
        
    try:
        summary = open(summary,"a+")
    except OSError:
        print("could not open summary to append ", summary)
        sys.exit()
    
    out = parsePdf(ffile)
    print(out)


   # chinaNumbers.insert(0,'china')
  #  chinaNumbers.insert(0,date)
  #  chinaVals = ",".join(str(x) for x in chinaNumbers)
    chinaVals = 0
    
    try:
        if runmode > 0: 
            summary.write(chinaVals + "\n")
    except OSError:
        print("could not append ", summary)
        sys.exit()

    try:
        if runmode > 0:
            print("update filelist ")
            fl.write(f + "\n")
    except OSError:
        print("could not append ", filelist)
        sys.exit()
        
    try:
        summary.close()
    except OSError:
        print("could not close summary ", summary)
        sys.exit()

    try:
        fl.close()
    except OSError:
        print("could not close file list ", filelist)
        sys.exit()
        
    return chinaVals
