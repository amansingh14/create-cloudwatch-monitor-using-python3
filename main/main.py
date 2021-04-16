# Author : Aman Singh
# Org : nClouds Inc.

import json
import boto3
import variable
import ec2_Monitor
monitor = boto3.resource('cloudwatch')
cloudwatch = boto3.client('cloudwatch')
ec2 = boto3.resource('ec2')

instance_list = []
cloudwatch_monitor_list = []

if variable.ec2 :
    for instance in ec2.instances.all():  
        instance_list.append(instance.id)            
        
    for alarm_iterator in monitor.alarms.all():
        cloudwatch_monitor_list.append(alarm_iterator.name)

    ec2_monitor.create_CPU_monitor(instance_list)
    ec2_monitor.create_DiskReadOps_monitor(instance_list)
    ec2_monitor.create_DiskWriteOps_monitor(instance_list)
    ec2_monitor.create_CPUCreditUsage_monitor(instance_list)

