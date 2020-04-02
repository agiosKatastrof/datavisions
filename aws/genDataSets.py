#!/usr/bin/env python

import sys, getopt
import json
import datetime
import pandas as pd
import numpy as np

from gendata import genCurve
from datetime import datetime, timedelta, date

def main(argv):

    instances = ['i-0ca364ec6656ff517','i-089389afc8097dac4','i-09f0182499b5eaf27']
    startt = '03/01/2020 00:00:00'
    endt = '03/31/2020 23:59:59'
    incMin = 10
    startt = datetime.strptime(startt, '%m/%d/%Y %H:%M:%S')
    endt = datetime.strptime(endt, '%m/%d/%Y %H:%M:%S')
    
    times = []
    delta = timedelta(minutes=incMin)
    while startt <= endt:
        times.append(startt)
        startt += delta

    n = len(times)
#def genCurve(seed,max,min,incFactor,n,incWeights):

    incWeights1 = [-1,-1,-1,1]
    incWeights2 = [-1,-0.5,.75,1]
    incWeights3 = [-1,-1,-1,1]
    out1 = genCurve(0.5,1,0,0.1,n,incWeights1)   
    out2 = genCurve(0.8,.9,0,0.1,n,incWeights2)   
    out3 = genCurve(0.1,.4,0,0.1,n,incWeights3)   


    data = {'datetime':times, instances[0]:out1, instances[1]:out2, instances[2]:out3}
    df = pd.DataFrame(data)
    print(df.head(10))
    print(df.describe())
    print(df.info)
    df.to_csv('/home/joe/data/aws/out.csv', index=False)

if __name__ == "__main__":
    main(sys.argv[1:])
