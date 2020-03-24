import boto3

service = boto3.resource('ec2')

def getEC2Instances(instanceStates = [], *args):

    returnThis = {}

    instances = service.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': instanceStates}])


    for instance in instances:
        #print(dir(instance))
        returnThis[instance.id] = {'type': instance.instance_type, 'state': instance.state['Name'], 'launch_time': instance.launch_time}
       # print(instance.id, instance.instance_type, instance.state['Name'], instance.launch_time)

    return returnThis 


