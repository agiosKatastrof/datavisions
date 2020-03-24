#!/usr/bin/env python

import sys, getopt
import json

from cloudwatch import getMetricStats
instanceId = 'i-0ca364ec6656ff517'
metric = 'CPUUtilization'
namespace = 'AWS/EC2'
startt = '2020-03-23T01:00:00'
endt = '2020-03-24T01:00:00'
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
