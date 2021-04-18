# Author : Aman Singh
# Org : nClouds Inc.

import json
import boto3
import Variable_Service
import ec2_Monitor
import Variable_Function
ec2 = boto3.resource('ec2')

instance_list = []

if Variable_Service.ec2 :
    for instance in ec2.instances.all():  
        instance_list.append(instance.id)            
        
if Variable_Function.Create_CPU_Monitor :
    ec2_Monitor.Create_CPU_Monitor(instance_list)

if Variable_Function.Ceate_DiskReadOps_Monitor :
    ec2_Monitor.Ceate_DiskReadOps_Monitor(instance_list)

if Variable_Function.Create_DiskWriteOps_Monitor :
    ec2_Monitor.Create_DiskWriteOps_Monitor(instance_list)

if Variable_Function.Create_CPUCreditUsage_Monitor : 
    ec2_Monitor.Create_CPUCreditUsage_Monitor(instance_list)

