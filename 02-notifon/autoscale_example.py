# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
autoscale = boto3.client('autoscaling')
response = autoscale.create_autoscaling_group(AutoscalingGroupName='Boto3Autoscaling')
response = autoscale.create_auto_scaling_group(AutoscalingGroupName='Boto3Autoscaling')
session = boto3.Session(profile_name='pythonAutomation')
as_client = session.client('autoscaling')
as_client.describe_auto_scaling_groups()
as_client.execute_policy(AutoScalingGroupName='NotifonExample', PolicyName='Scale Down')
as_client.execute_policy(AutoScalingGroupName='NotifonExample', PolicyName='Scale Up')
as_client.execute_policy(AutoScalingGroupName='NotifonExample', PolicyName='Scale Up')
as_client.execute_policy(AutoScalingGroupName='NotifonExample', PolicyName='Scale Up')
as_client.execute_policy(AutoScalingGroupName='NotifonExample', PolicyName='Scale Up')
