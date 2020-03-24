#!/usr/bin/env python

import sys, getopt
import json
import datetime

from cloudwatch import getMetricStats
from ec2 import getEC2Instances

instanceId = 'i-0ca364ec6656ff517'
metric = 'CPUUtilization'
namespace = 'AWS/EC2'
startt = datetime.datetime(2020,3,21,23)
endt = datetime.datetime(2020,3,24,23)
period = 300
stats = 'Maximum'
unit = 'Percent'

instanceStates = ['running','stopped','rebooting','shuttding-down','terminated','stopping']

def main(argv):
    usage = 'aws.py <-i|-u>'

    verbose = None

    try:
        opts, args = getopt.getopt(argv,"iuv")
    except:
        print(usage)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt == '-i':
            print('get instances only')                   
            for instance in getEC2Instances(instanceStates).items():
                print(instance)
            sys.exit(0)
        elif opt == '-u':
            #print('get instances and utilizations')
            for instanceId in getEC2Instances(instanceStates):
                #print('get metrics for ', instanceId)
                response = getMetricStats(instanceId,metric,namespace,startt,endt,period,stats,unit)
                for item in response['Datapoints']:
                    print(item['Timestamp'],end=",")
                    print(instanceId,end=",")
                    print(item[stats])


if __name__ == "__main__":
    main(sys.argv[1:])
