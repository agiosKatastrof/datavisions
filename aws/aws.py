#!/usr/bin/env python

import sys, getopt
import json
import datetime

from cloudwatch import getMetricStats
from ec2 import getEC2Instances



instanceStates = ['running','stopped','rebooting','shuttding-down','terminated','stopping']

def main(argv):
    usage = 'aws.py -i -s <"YYYY-MM-DD HH:MM"> -e <"YYYY-MM-DD HH:MM"> -m <metric> -n <namespace> -p <period>'

    #defaults
    getInstancesOnly = None

    startt = datetime.datetime(2020,3,21,23)
    endt = datetime.datetime(2020,3,24,23)
    metric = 'CPUUtilization'
    namespace = 'AWS/EC2'
    period = 300
    stats = 'Maximum'
    unit = 'Percent'

    try:
        opts, args = getopt.getopt(argv,"is:e:m:n:p:")
    except:
        print(usage)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt == '-i':
            print('get instances only') 
            getInstancesOnly = 1                  
        elif opt == '-s':
            startt = arg
        elif opt == '-e':
            endt = arg
        elif opt == '-m':
            metric = arg
        elif opt == '-n':
            namespace = arg
        elif opt == '-p':
            period = arg

    if (getInstancesOnly):
        for instance in getEC2Instances(instanceStates).items():
            print(instance)
        sys.exit(0)
    else:
        for instanceId in getEC2Instances(instanceStates):
            response = getMetricStats(instanceId,metric,namespace,startt,endt,period,stats,unit)
            for item in response['Datapoints']:
                print(item['Timestamp'],end=",")
                print(instanceId,end=",")
                print(item[stats])        

if __name__ == "__main__":
    main(sys.argv[1:])
