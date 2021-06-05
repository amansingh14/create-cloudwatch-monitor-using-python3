
# This file has following functions:
# 1. Create_LBD_Error(dict function_list)
# 2. Create_LBD_Throttles(dict function_list)
# 3. Create_LBD_Invocations(dict function_list)
# 4. Create_LBD_Duration(dict function_list)
# 5. Create_LBD_ConcurrentExecutions(dict function_list)
# 6. Create_LBD_UnreservedConcurrentExecutions(dict function_list)

####

import boto3
#import Variable_Monitor
monitor = boto3.resource('cloudwatch')
cloudwatch = boto3.client('cloudwatch')
import re

Cloudwatch_Monitor_List = []

# function to create Error Count Alarm.

def Create_LBD_Error(lambda_function_list):
    for alarm_iterator in monitor.alarms.all():
        Cloudwatch_Monitor_List.append(alarm_iterator.name)

    Monitor_List = str(Cloudwatch_Monitor_List)
    for lbd in lambda_function_list: 
        if list(set(re.findall(r'Error count is high on*(?: *([\w.-]+))?', Monitor_List.lower()))):
            print('ELB Latency Alarm is Present for :', lbd)
            
        else:
            cloudwatch.put_metric_alarm(
                AlarmName='Error Count is High on %s' % lbd,
                ComparisonOperator='GreaterThanOrEqualToThreshold',
                EvaluationPeriods=1,
                MetricName='Errors',
                Namespace='AWS/Lambda',
                Period=60,
                Statistic='Average',
                Threshold=10.0,
                ActionsEnabled=False,
                AlarmDescription='Error Count spike over 10',
                Dimensions=[
                {
                    'Name': 'Lambda_Name',
                    'Value': lbd
                },
                ],
                Tags=[
                {
                    'Key': 'type',
                    'Value': 'Errors'
                },
                {
                    'Key': 'Name',
                    'Value': lbd
                }           
                ],
                Unit='Seconds'
                )
            print("Error Count Alarm Successfully created for :", lbd)
    print("==========================================")

# function to create Throttle Alarm

def Create_LBD_Throttles(lambda_function_list):
    for alarm_iterator in monitor.alarms.all():
        Cloudwatch_Monitor_List.append(alarm_iterator.name)

    Monitor_List = str(Cloudwatch_Monitor_List)
    for lbd in lambda_function_list: 
        if list(set(re.findall(r'Throttle is high on*(?: *([\w.-]+))?', Monitor_List.lower()))):
            print('RequestCount Alarm is Present for :', lbd)
            
        else:
            cloudwatch.put_metric_alarm(
                AlarmName='Throttle is High on %s' % lbd,
                ComparisonOperator='GreaterThanOrEqualToThreshold',
                EvaluationPeriods=1,
                MetricName='Throttles',
                Namespace='AWS/Lambda',
                Period=60,
                Statistic='Average',
                Threshold=1.0,
                ActionsEnabled=False,
                AlarmDescription='Alarm when Throttle is greater than equal to 1',
                Dimensions=[
                {
                    'Name': 'Lambda_Name',
                    'Value': lbd
                },
                ],
                Tags=[
                {
                    'Key': 'type',
                    'Value': 'Throttles'
                },
                {
                    'Key': 'Name',
                    'Value': lbd
                }           
                ],
                
                )
            print("Throttle Alarm Successfully created for :", lbd)
    print("==========================================")

# function to create Invocations alarm
def Create_LBD_Invocations(lambda_function_list):
    for alarm_iterator in monitor.alarms.all():
        Cloudwatch_Monitor_List.append(alarm_iterator.name)

    Monitor_List = str(Cloudwatch_Monitor_List)
    for lbd in lambda_function_list: 
        if list(set(re.findall(r'Invocation is high on*(?: *([\w.-]+))?', Monitor_List.lower()))):
            print('Invocation Alarm is Present for :', lbd)
            
        else:
            cloudwatch.put_metric_alarm(
                AlarmName='Invocation is High on %s' % lbd,
                ComparisonOperator='GreaterThanOrEqualToThreshold',
                EvaluationPeriods=1,
                MetricName='Invocations',
                Namespace='AWS/Lambda',
                Period=60,
                Statistic='Average',
                Threshold=1.0,
                ActionsEnabled=False,
                AlarmDescription='Alarm when Invocations is greater than equal to 5',
                Dimensions=[
                {
                    'Name': 'Lambda_Name',
                    'Value': lbd
                },
                ],
                Tags=[
                {
                    'Key': 'type',
                    'Value': 'Invocations'
                },
                {
                    'Key': 'Name',
                    'Value': lbd
                }           
                ],
                
                )
            print("Invocations Alarm Successfully created for :", lbd)
    print("==========================================")

# Function to create Duration alarm
def Create_LBD_Duration(lambda_function_list):
    for lbd in lambda_function_list: 
        if list(set(re.findall(r'Duration is high on*(?: *([\w.-]+))?', Monitor_List.lower()))):
            print('Invocation Alarm is Present for :', lbd)
            
        else:
            cloudwatch.put_metric_alarm(
                AlarmName='Duration is High on %s' % lbd,
                ComparisonOperator='GreaterThanOrEqualToThreshold',
                EvaluationPeriods=1,
                MetricName='Invocations',
                Namespace='AWS/Lambda',
                Period=60,
                Statistic='Average',
                Threshold=5.0,
                ActionsEnabled=False,
                AlarmDescription='Alarm when Duration is greater than equal to 5',
                Dimensions=[
                {
                    'Name': 'Lambda_Name',
                    'Value': lbd
                },
                ],
                Tags=[
                {
                    'Key': 'type',
                    'Value': 'Duration'
                },
                {
                    'Key': 'Name',
                    'Value': lbd
                }           
                ],
                
                )
            print("Invocations Alarm Successfully created for :", lbd)
    print("==========================================")
# Function to create ConcurrentExecutions alarm

def Create_LBD_ConcurrentExecutions(lambda_function_list) :
    for lbd in lambda_function_list: 
        if list(set(re.findall(r'ConcurrentExecutions is high on*(?: *([\w.-]+))?', Monitor_List.lower()))):
            print('ConcurrentExecutions Alarm is Present for :', lbd)
            
        else:
            cloudwatch.put_metric_alarm(
                AlarmName='Duration is High on %s' % lbd,
                ComparisonOperator='GreaterThanOrEqualToThreshold',
                EvaluationPeriods=1,
                MetricName='ConcurrentExecutions',
                Namespace='AWS/Lambda',
                Period=60,
                Statistic='Average',
                Threshold=5.0,
                ActionsEnabled=False,
                AlarmDescription='Alarm when Duration is greater than equal to 5',
                Dimensions=[
                {
                    'Name': 'Lambda_Name',
                    'Value': lbd
                },
                ],
                Tags=[
                {
                    'Key': 'type',
                    'Value': 'ConcurrentExecutions'
                },
                {
                    'Key': 'Name',
                    'Value': lbd
                }           
                ],
                
                )
            print("ConcurrentExecutions Alarm Successfully created for :", lbd)
    print("==========================================")
# Function to create UnreservedConcurrentExecutions alarm
   
def Create_LBD_UnreservedConcurrentExecutions(lambda_function_list):
    for lbd in lambda_function_list: 
        if list(set(re.findall(r'UnreservedConcurrentExecutions is high on*(?: *([\w.-]+))?', Monitor_List.lower()))):
            print('ConcurrentExecutions Alarm is Present for :', lbd)
            
        else:
            cloudwatch.put_metric_alarm(
                AlarmName='Duration is High on %s' % lbd,
                ComparisonOperator='GreaterThanOrEqualToThreshold',
                EvaluationPeriods=1,
                MetricName='UnreservedConcurrentExecutions',
                Namespace='AWS/Lambda',
                Period=60,
                Statistic='Average',
                Threshold=5.0,
                ActionsEnabled=False,
                AlarmDescription='Alarm when UnreservedConcurrentExecutions is greater than equal to 5',
                Dimensions=[
                {
                    'Name': 'Lambda_Name',
                    'Value': lbd
                },
                ],
                Tags=[
                {
                    'Key': 'type',
                    'Value': 'UnreservedConcurrentExecutions'
                },
                {
                    'Key': 'Name',
                    'Value': lbd
                }           
                ],
                
                )
            print("UnreservedConcurrentExecutions Alarm Successfully created for :", lbd)
    print("==========================================")

   