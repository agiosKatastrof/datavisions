#!/usr/bin/env python

import sys, getopt
import json
import datetime
import pandas as pd
import numpy as np

from gendata import genCurve
from datetime import datetime, timedelta, date

def main(argv):
    usage = 'aws.py -s <seed> -x <max> -m <min> -i <inc> -n <n>'

    instances = ['i-0ca364ec6656ff517','i-089389afc8097dac4','i-09f0182499b5eaf27']
    startt = '03/01/2020 00:00:00'
    endt = '03/31/2020 23:59:59'
    incMin = 10
    startt = datetime.strptime(startt, '%m/%d/%Y %H:%M:%S')
    endt = datetime.strptime(endt, '%m/%d/%Y %H:%M:%S')


    try:
        opts, args = getopt.getopt(argv,"s:x:m:i:n:")
    except:
        print(usage)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt == '-s':
            start = float(arg)              
        elif opt == '-x':
            maxV = float(arg)
        elif opt == '-m':
            minV = float(arg)
        elif opt == '-i':
            inc = float(arg)
        elif opt == '-n':
            n = int(arg)
    
    
    delta = timedelta(minutes=incMin)
    while startt <= endt:
        print(startt)
        startt += delta

  
    out = genCurve(start,maxV,minV,inc,n)   
    print(out) 

if __name__ == "__main__":
    main(sys.argv[1:])
