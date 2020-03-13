#!/usr/bin/env python

from covid19 import findFilesToProcess, parsePdf, findFilesToProcess, processFile

mypath = '/home/joe/data/covid19/who'   #where the pdfs are
#mypath = '/run/user/1000/gvfs/smb-share:server=majesty.local,share=filesjoe/data/who_covid19_reports/renamed'
filelist = '/home/joe/data/covid19/filelist'  # list of processed files
summary = '/home/joe/data/covid19/summary' # summary data

dfToProcess = findFilesToProcess(mypath,filelist)
rows, columns = dfToProcess.shape

runmode = 0 # does not write

if (rows > 0): #there are files to process
    #f = dfToProcess['file'].iloc[0]  # just do one file
    for f in dfToProcess['file'].tolist():   
        print("found to process: ", f)
        out = processFile(mypath,filelist,summary,f,runmode)
        print("output: ", out) 

exit(0)
