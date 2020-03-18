#!/usr/bin/env python

import sys, getopt
import re
import os
from os import listdir
from os.path import isfile, join

def main(argv):
    inputdir = None
    outputdir = None
    write = None

    usage = 'renamePdfs.py -i <inputdir> -o <outputdir> -write'

    try:
        opts, args = getopt.getopt(argv,"hwi:o:",["indir=","outdir="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt == '-w':
            write = 1
        elif opt in ("-i", "--idir"):
            inputdir = arg
        elif opt in ("-o", "--ofile"):
            outputdir = arg

    files = [f for f in listdir(inputdir) if isfile(join(inputdir, f))]
    for f in files:
        match = re.match(r"\d{8}",f)
        yr = match[0][0:4]
        mo = match[0][4:6]
        dy = match[0][6:8]
        newfname = yr + "-" + mo + "-" + dy + ".pdf"
        ffile = inputdir + "/" + f
        fnewfname = outputdir + "/" + newfname

        if (write):
            print(ffile, " -> ", fnewfname)
            os.rename(ffile,fnewfname)
        else:
            print("would have ", ffile, " -> ", fnewfname)


if __name__ == "__main__":
   main(sys.argv[1:])
