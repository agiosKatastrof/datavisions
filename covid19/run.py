#!/usr/bin/env python
#import sys
#sys.path.append("/home/joe/datavisions/covid19")
from covid19 import findFilesToProcess, parsePdf, findFilesToProcess, processFile

#mypath = '/home/joe/data/covid19/who'
mypath = '/home/joe/data/covid19/who/test'
#mypath = '/run/user/1000/gvfs/smb-share:server=majesty.local,share=filesjoe/data/who_covid19_reports/renamed'
filelist = '/home/joe/datavisions/covid19/filelist'
summary = '/home/joe/data/covid19/summary'
#dill.dump_session('data.db')
#dill.load_session('data.db')

#dfToProcess = findFilesToProcess(mypath,filelist)
#rows, columns = dfToProcess.shape

#if (rows > 0): #there are files to process
    #f = dfToProcess['file'].iloc[0]  # just do one file
    
#    for f in dfToProcess['file'].tolist():   
#        print("found to process: ", f)
 #       out = processFile(mypath,filelist,summary,f)
 #       print("output: ", out) 
