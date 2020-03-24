import boto3
import datetime

def getMetrics(InstanceId,metric,namespace,startt,endt):
    print('get metrics')
    cw = boto3.client('cloudwatch')

    response = cw.get_metric_statistics(
        Namespace=namespace,
        MetricName=metric,
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': InstanceId
            },
        ],
        StartTime=startt,
        EndTime=endt,
        Period=360,
        Statistics=[
            'Maximum',
        ],
        Unit='Percent'
)

    return response
