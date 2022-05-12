# coding: utf-8
get_ipython().run_line_magic('pwd', '')
import boto3
session = boto3.Session(profile_name='pythonAutomation')
ec2 = session.resource('ec2')
key_name = 'python_automation_key'
key_path = key_name + '.pem'
key = ec2.create_key_pair(KeyName=key_name)
key.key_material
with open(key_path, 'w') as key_file:
    key_file.write(key.ley_material)
    
with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)
    
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
import os, stat
os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)
get_ipython().run_line_magic('ls', '-l python_automation_key.pem')
ec2.images.filter(Owners=['amazon'])
list(ec2.images.filter(Owners=['amazon']))
len(list(ec2.images.filter(Owners=['amazon'])))
img = ec2.Image('ami-0fa49cc9dc8d62c84')
img.name
img = ec2.Image('ami-0022f774911c1d690')
img.name
img.name
ami_name = "amzn2-ami-kernel-5.10-hvm-2.0.20220426.0-x86_64-gp2"
filters = [{'Name': 'name', 'Values': [ami_name]}]
list(ec2.images.filter(Owners=['amazon'], Filters=filters))
img
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.keyname)
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name)
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name, SubnetId='subnet-110b0c5a')
instances
inst = instances[0]
inst
inst.terminate()
instances = ec2.create_instances(ImageId=img.id, MinCount=1, MaxCount=1, InstanceType='t2.micro', KeyName=key.key_name, SubnetId='subnet-110b0c5a')
inst = instances[0]
inst.public_dns_name
inst.public_dns_name
inst.wait_until_running()
inst.reload()
inst.public_dns_name
inst.security_groups
# Look up security group
#Authorize incoming connections from our public IP address, on port 22(the sport SSH uses)
inst.security_groups.all()
ec2.security_groups.all()
inst.security_groups
sg = ec2.SecurityGroup(inst.security_groups[0]['GroupId'])
sg.authorize_ingress(IpPermissions=[{'FromPort':22, 'ToPort':22, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp': '38.88.227.234/32'}]}]
sg.authorize_ingress(IpPermissions=[{'FromPort':22, 'ToPort':22, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp': '38.88.227.234/32'}]}])
inst.security_groups
inst = instances[0]
key.key_name
sg.authorize_ingress(IpPermissions=[{'FromPort':80, 'ToPort':80, 'IpProtocol':'TCP', 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}])
inst.public_dns_name
