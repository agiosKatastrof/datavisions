import boto3
import datetime

def getMetrics(InstanceId):
    print('get metrics')
    cw = boto3.client('cloudwatch')

    response = cw.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': InstanceId
            },
        ],
        StartTime='2020-03-22T23:23:00',
        EndTime='2020-03-23T23:23:00',
        Period=360,
        Statistics=[
            'Maximum',
        ],
        Unit='Percent'
)

    return response
