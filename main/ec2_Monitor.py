# Author : Aman Singh
# Org : nClouds Inc.

import boto3
monitor = boto3.resource('cloudwatch')
cloudwatch = boto3.client('cloudwatch')
import re

Cloudwatch_Monitor_List = []



# Create CPU Utilization for EC2 instance metric alert.

def Create_CPU_Monitor(instance_list):
    for alarm_iterator in monitor.alarms.all():
        Cloudwatch_Monitor_List.append(alarm_iterator.name)

    Monitor_List = str(Cloudwatch_Monitor_List)
    for instance_id in instance_list: 
        if list(set(re.findall(r'cpu utilization is high on*(?: *([\w.-]+))?', Monitor_List.lower()))):
            print('CPU Utilization monitor Found for:', instance_id)
            
        else:     
            cloudwatch.put_metric_alarm(
                AlarmName='EC2 : CPU Utilization is HIGH on %s' % instance_id,
                ComparisonOperator='GreaterThanThreshold',
                EvaluationPeriods=1,
                MetricName='CPUUtilization',
                Namespace='AWS/EC2',
                Period=60,
                Statistic='Average',
                Threshold=70.0,
                ActionsEnabled=False,
                AlarmDescription='Alarm when server CPU exceeds 70%',
                Dimensions=[
                {
                    'Name': 'Instance_ID',
                    'Value': instance_id
                },
                ],
                Tags=[
                {
                    'Key': 'type',
                    'Value': 'CPUUtilization'
                },
                {
                    'Key': 'Name',
                    'Value': instance_id
                }           
                ],
                Unit='Seconds'
                )
            print("CPU monitor Created successfully for EC2 instance:", instance_id)

# # Create DISK READOPS for EC2 Instance metric alert. 

def Ceate_DiskReadOps_Monitor(instance_list):
     for alarm_iterator in monitor.alarms.all():
        Cloudwatch_Monitor_List.append(alarm_iterator.name)

    Monitor_List = str(Cloudwatch_Monitor_List)
    for instance_id in instance_list: 
        if list(set(re.findall(r'DiskReadIOPS is high on*(?: *([\w.-]+))?', Monitor_List.lower()))):
            print('DiskReadOps monitor Found for:', instance_id)
            
        else:  
        cloudwatch.put_metric_alarm(
            AlarmName='EC2 : DiskReadIOPS is HIGH on %s' % instance_id,
            ComparisonOperator='GreaterThanOrEqualToThreshold',
            EvaluationPeriods=1,
            MetricName='DiskReadOps',
            Namespace='AWS/EC2',
            Period=60,
            Statistic='Average',
            Threshold=70.0,
            ActionsEnabled=False,
            AlarmDescription='Alarm when DiskReadOps exceeds 70',
            Dimensions=[
            {
                'Name': 'Instance_ID',
                'Value': instance_id
            },
            ],
            Tags=[
            {
                'Key': 'type',
                'Value': 'DiskReadOps'
            },
            {
                'Key': 'Name',
                'Value': instance_id
            }           
            ],
            Unit='Seconds'
            )
        print("DisReadOps Monitor Created successfully for instance: ", instance_id)


# #
def Create_DiskWriteOps_Monitor(instance_list):
    for instance_id in instance_list:
        cloudwatch.put_metric_alarm(
            AlarmName='EC2 : Disk Read IOPS is HIGH on %s' % instance_id,
            ComparisonOperator='GreaterThanOrEqualToThreshold',
            EvaluationPeriods=1,
            MetricName='DiskWriteOps',
            Namespace='AWS/EC2',
            Period=60,
            Statistic='Average',
            Threshold=70.0,
            ActionsEnabled=False,
            AlarmDescription='Alarm when DiskWriteOps exceeds 70',
            Dimensions=[
            {
                'Name': 'Instance_ID',
                'Value': instance_id
            },
            ],
            Tags=[
            {
                'Key': 'type',
                'Value': 'DiskReadOps'
            },
            {
                'Key': 'Name',
                'Value': instance_id
            }           
            ],
            Unit='Seconds'
            )
        print("DiskWriteOps Monitor Created successfully for instance: ", instance_id)

# CPUCreditUsage

def Create_CPUCreditUsage_Monitor(instance_list):
    for instance_id in instance_list:
        cloudwatch.put_metric_alarm(
            AlarmName='EC2 : CPUCreditUsage is HIGH on %s' % instance_id,
            ComparisonOperator='GreaterThanOrEqualToThreshold',
            EvaluationPeriods=1,
            MetricName='CPUCreditUsage',
            Namespace='AWS/EC2',
            Period=60,
            Statistic='Average',
            Threshold=1,
            ActionsEnabled=False,
            AlarmDescription='Alarm when CPUCreditUsage exceeds 2',
            Dimensions=[
            {
                'Name': 'Instance_ID',
                'Value': instance_id
            },
            ],
            Tags=[
            {
                'Key': 'type',
                'Value': 'DiskReadOps'
            },
            {
                'Key': 'Name',
                'Value': instance_id
            }           
            ],
            Unit='Seconds'
            )
        print("CPUCreditUsage Monitor Created successfully for instance: ", instance_id)
