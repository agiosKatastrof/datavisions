import json

with open('/home/joe/data/aws/ec2_types.json') as f:
  data = json.load(f)

for InstanceType in data["InstanceTypes"]:
    print(InstanceType["InstanceType"],",",end='')
    print(InstanceType["VCpuInfo"]["DefaultVCpus"],",",end='')
    print(InstanceType["MemoryInfo"]['SizeInMiB'])
  