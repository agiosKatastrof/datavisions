import boto3

def getMetricStats(InstanceId,metric,namespace,startt,endt,period,stats,unit):
    print('get ', metric, ' for ', InstanceId)
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
        Period=period,
        Statistics=[
            stats,
        ],
        Unit=unit
)

    return response
