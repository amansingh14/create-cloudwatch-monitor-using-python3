# Author : Aman Singh
# Org : nClouds Inc.

import json
import boto3

#Import variable checks 
import Variable.Variable_Service
import Variable.Variable_Function

#Import Alarm Functions

import monitor.ec2_Alarms
import monitor.elb_Alarms


if Variable.Variable_Service.ec2 :
    ec2 = boto3.resource('ec2')
    instance_list = []

    for instance in ec2.instances.all():  
        instance_list.append(instance.id)            
        
    if Variable.Variable_Function.ec2_CPU_Monitor :
        monitor.ec2_Alarms.Create_CPU_Monitor(instance_list)

    if Variable.Variable_Function.ec2_DiskReadOps_Monitor :
        monitor.ec2_Alarms.Create_DiskReadOps_Monitor(instance_list)

    if Variable.Variable_Function.ec2_DiskWriteOps_Monitor :
        monitor.ec2_Alarms.Create_DiskWriteOps_Monitor(instance_list)

    if Variable.Variable_Function.ec2_CPUCreditUsage_Monitor : 
        monitor.ec2_Alarms.Create_CPUCreditUsage_Monitor(instance_list)


if Variable.Variable_Service.elb :
    elb_list = []
    elbList = boto3.client('elb')
    elb_json = elbList.describe_load_balancers()
    for elb in elb_json['LoadBalancerDescriptions']:
        elb_list.append(elb['LoadBalancerName'])
    
    if Variable.Variable_Function.ELB_Latency:
        monitor.elb_Alarms.Create_ELB_Latency(elb_list)

    if Variable.Variable_Function.ELB_RequestCount :
        monitor.elb_Alarms.Create_ELB_RequestCount(elb_list)

    if Variable.Variable_Function.ELB_UnHealthyHostCount :
        monitor.elb_Alarms.Create_ELB_UnHealthyHostCount(elb_list)

    if Variable.Variable_Function.ELB_HTTPCode_ELB_5XX : 
        monitor.elb_Alarms.Create_ELB_HTTPCode_ELB_5XX(elb_list)
    