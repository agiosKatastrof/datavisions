#!/usr/bin/env python

import sys, getopt
import json
import datetime

from scale import genWeight

scaleFactor = 100
scaleRange = [10,9,8,7,6,5,3,1]

weight = genWeight(scaleFactor,scaleRange)
print(weight)