#!/usr/bin/env python

import sys, getopt

from cloudwatch import getMetrics

def main(argv):

    usage = 'run.py -r -d <datadir> -f <filelist> -s <summary>'
    getMetrics()

if __name__ == "__main__":
    main(sys.argv)
