#!/usr/bin/env python

import sys

from covid19 import findFilesToProcess, parsePdf, findFilesToProcess, processFile

mypath = '/home/joe/data/covid19/who/actual'   #where the pdfs are
filelist = '/home/joe/data/covid19/filelist'  # list of processed files
summary = '/home/joe/data/covid19/summary' # summary data

def main(argv):

    runmode = 0 # does not write, value of >0 writes
    if (len(sys.argv) > 1):
        print("writing files")
        runmode = 1

    dfToProcess = findFilesToProcess(mypath,filelist)
    rows, columns = dfToProcess.shape


    if (rows > 0): #there are files to process
        #f = dfToProcess['file'].iloc[0]  # just do one file
        for f in dfToProcess['file'].tolist():   
            print("found to process: ", f)
            out = processFile(mypath,filelist,summary,f,runmode)
            print("output: ", out) 

if __name__ == "__main__":
    main(sys.argv[1:])