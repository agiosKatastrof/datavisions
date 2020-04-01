#!/usr/bin/env python

import sys, getopt
import json
import datetime

from scale import boundaryScale, genWeight

scaleFactor = 100
scaleRange = [10,8,5,1]


inN = [0.11,0.22,0.1234,0.0,0.5]

#outN = boundaryScale(scaleFactor,scaleRange, inN,0.11)
#print(outN)

w = genWeight(scaleFactor,scaleRange)

print(w)

