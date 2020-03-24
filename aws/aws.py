#!/usr/bin/env python

import sys, getopt
import json
import datetime

from cloudwatch import getMetricStats
instanceId = 'i-0ca364ec6656ff517'
metric = 'CPUUtilization'
namespace = 'AWS/EC2'
startt = datetime.datetime(2020,3,23,1)
endt = datetime.datetime(2020,3,24,1)
period = 300
stats = 'Maximum'
unit = 'Percent'

def main(argv):
    response = getMetricStats(instanceId,metric,namespace,startt,endt,period,stats,unit)
    for item in response['Datapoints']:

        print(item['Timestamp'],end=",")
        print(instanceId,end=",")
        print(item[stats])


if __name__ == "__main__":
    main(sys.argv)
