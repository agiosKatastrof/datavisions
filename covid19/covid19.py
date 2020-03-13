import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tabula
import dill
import re
import sys
import csv
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
    
    tables = tabula.read_pdf(f, pages = "all", multiple_tables = True)
    chinaNumbers = findChina(tables)
       
    return chinaNumbers   

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

def processFile(mypath,filelist,summary,f):
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
    
    chinaNumbers = parsePdf(ffile)
    chinaNumbers.insert(0,'china')
    chinaNumbers.insert(0,date)
    chinaVals = ",".join(str(x) for x in chinaNumbers)
    
    try:
        summary.write(chinaVals + "\n")
    except OSError:
        print("could not append ", summary)
        sys.exit()

    try:
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
