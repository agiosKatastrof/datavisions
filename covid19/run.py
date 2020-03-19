#!/usr/bin/env python

import sys, getopt

from covid19 import findFilesToProcess, parsePdf, findFilesToProcess, processFile

mypath = '/home/joe/data/covid19/who/actual'   #where the pdfs are
filelist = '/home/joe/data/covid19/filelist'  # list of processed files
summary = '/home/joe/data/covid19/summary' # summary data

def main(argv):

    runmode = 0
    datadir = None
    filelist = None
    summary = None

    usage = 'run.py -r -d <datadir> -f <filelist> -s <summary>'

    try:
        opts, args = getopt.getopt(argv,"rd:f:s:",["d=","f=","s="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt == '-r':
            runmode = 1
            print("doing an actual run")
        elif opt in ("-d"):
            datadir = arg
        elif opt in ("-f"):
            filelist = arg
        elif opt in ("-s"):
            summary = arg

    dfToProcess = findFilesToProcess(datadir,filelist)
    rows, columns = dfToProcess.shape

    if (rows > 0): #there are files to process
        for f in dfToProcess['file'].tolist():   
            print("found to process: ", f)
            out = processFile(datadir,filelist,summary,f,runmode)
            print("output: ", out) 

if __name__ == "__main__":
    main(sys.argv[1:])