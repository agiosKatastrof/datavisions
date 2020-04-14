import json

with open('/home/joe/data/aws/ec2_types.json') as f:
  data = json.load(f)

for InstanceType in data["InstanceTypes"]:
    print(InstanceType, "\n")
    print(InstanceType["VCpuInfo"], "\n")
    print(InstanceType["MemoryInfo"], "\n")