#!/usr/bin/env python

import sys, getopt

from cloudwatch import getMetrics
id = 'i-0ca364ec6656ff517'


def main(argv):

    usage = 'run.py -r -d <datadir> -f <filelist> -s <summary>'
    response = getMetrics(id)
    print(response)

if __name__ == "__main__":
    main(sys.argv)
