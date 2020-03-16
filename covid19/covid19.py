import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tabula
import dill
import re
import sys
import csv
import subprocess
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
    date = 'N/A'
    i = 0
    date = None
    for l in outlist: 
        l = str(l)

        # find the date 
        if (date is None):
            date = findDate(l)

            if (date is not None):
                print(date)
            
        # find China 
        pattern = 'China'
        china = re.search(pattern,l)
        if(china):
            print(i, " china ",china.group())
            nextl = str(outlist[i+1])
            pattern = '\d+\s*\d+\s+confirmed'
            chinaConfirmed = re.search(pattern,nextl)


    
        i += 1
    return 

def findDate(l):
    returnDate = None
    print("looking for the date")
    pattern = '\s+\d+\s+\D+\s+2020'

    date = re.search(pattern,l)
    if(date):
        returnDate = date.group()
        print("found the date ", returnDate)

    return returnDate

def findChina(tables):
# from the list of tables (dfs), find the one with china - return cumulative cases and deaths
    x = 'Province/' # id China with this
    y = 'Hubei'# id China with this
    output = ['N/A','N/A']
    for df in tables:
        if (x in df.columns.values):
            if (y in df[x].tolist()):
                output = re.split('\\s+',df['Cumulative'].iloc[-1])
    return output

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
