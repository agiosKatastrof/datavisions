#!/usr/bin/env python

import sys, getopt

from cloudwatch import getMetrics
instanceId = 'i-0ca364ec6656ff517'
metric = 'CPUUtilization'
namespace = 'AWS/EC2'
startt = '2020-03-22T22:23:00'
endt = '2020-03-23T23:23:00'


def main(argv):
    response = getMetrics(instanceId,metric,namespace,startt,endt)
    print(response)

if __name__ == "__main__":
    main(sys.argv)
