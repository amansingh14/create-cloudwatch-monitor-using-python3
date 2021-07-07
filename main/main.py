# Author : Aman Singh
# Email: aman@nclouds.com
# Org : nClouds Inc.

import json
#from typing_extensions import TypeVarTuple
import boto3

#Import variable checks 
import Variable.Variable_Service
import Variable.Variable_Function

#Import Alarm Functions

import Alarms.ec2_Alarms
import Alarms.elb_Alarms
import Alarms.lambda_Alarms

#Function call to create EC2 instance Alarm. 

if Variable.Variable_Service.ec2 :
    ec2 = boto3.resource('ec2')
    instance_list = []

    for instance in ec2.instances.all():  
        instance_list.append(instance.id)            
        
    if Variable.Variable_Function.ec2_CPU_Monitor :
        Alarms.ec2_Alarms.Create_CPU_Monitor(instance_list)

    if Variable.Variable_Function.ec2_DiskReadOps_Monitor :
        Alarms.ec2_Alarms.Create_DiskReadOps_Monitor(instance_list)

    if Variable.Variable_Function.ec2_DiskWriteOps_Monitor :
        Alarms.ec2_Alarms.Create_DiskWriteOps_Monitor(instance_list)

    if Variable.Variable_Function.ec2_CPUCreditUsage_Monitor : 
        Alarms.ec2_Alarms.Create_CPUCreditUsage_Monitor(instance_list)

# Function call to create ELB Alarm.

if Variable.Variable_Service.elb :
    elb_list = []
    elbList = boto3.client('elb')
    elb_json = elbList.describe_load_balancers()
    for elb in elb_json['LoadBalancerDescriptions']:
        elb_list.append(elb['LoadBalancerName'])
    
    if Variable.Variable_Function.ELB_Latency:
        Alarms.elb_Alarms.Create_ELB_Latency(elb_list)

    if Variable.Variable_Function.ELB_RequestCount :
        Alarms.elb_Alarms.Create_ELB_RequestCount(elb_list)

    if Variable.Variable_Function.ELB_UnHealthyHostCount :
        Alarms.elb_Alarms.Create_ELB_UnHealthyHostCount(elb_list)

    if Variable.Variable_Function.ELB_HTTPCode_ELB_5XX : 
        Alarms.elb_Alarms.Create_ELB_HTTPCode_ELB_5XX(elb_list)

# Function call to create Lambda function Alarm.

if Variable.Variable_Service.lambda_function:
    lambda_function_list = []
    lambdafunction = boto3.client('lambda')
    
    lambda_json = lambdafunction.list_functions(
            #MasterRegion='us-east-1',
             FunctionVersion='ALL',
             MaxItems=100
        )

    for lbd in lambda_json['Functions']:
        lambda_function_list.append(lbd['FunctionName'])
        
    if Variable.Variable_Fuction.Lambda_Error :
        Alarms.lambda_Alarms.Create_LBD_Error(lambda_function_list)
    
    if Variable.Variable_Function.Lambda_Throttles : 
        Alarms.lambda_Alarms.Create_LBD_Throttles(lambda_function_list)
    
    if Variable.Variable_Function.Lambda_Invocations : 
        Alarms.lambda_Alarms.Create_LBD_Invocations(lambda_function_list)

    if Variable.Variable_Function.Lambda_Duration :
        Alarms.lambda_Alarms.Create_LBD_Duration(lambda_function_list)

    if Variable.Variable_Function.Lambda_ConcurrentExecutions :
        Alarms.lambda_Alarms.Create_LBD_ConcurrentExecutions(lambda_function_list)   

    if Variable.Variable_Function.Lambda_UnreservedConcurrentExecutions : 
        Alarms.lambda_Alarms.Create_LBD_UnreservedConcurrentExecutions(lambda_function_list)
