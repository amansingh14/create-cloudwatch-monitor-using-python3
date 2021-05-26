import boto3
#import Variable_Monitor
monitor = boto3.resource('cloudwatch')
cloudwatch = boto3.client('cloudwatch')
import re

Cloudwatch_Monitor_List = []

def Create_ELB_Latency(elb_list):
    for alarm_iterator in monitor.alarms.all():
        Cloudwatch_Monitor_List.append(alarm_iterator.name)

    Monitor_List = str(Cloudwatch_Monitor_List)
    for elb in elb_list: 
        if list(set(re.findall(r'elb latency is high on*(?: *([\w.-]+))?', Monitor_List.lower()))):
            print('ELB Latency Alarm is Present for :', elb)
            
        else:
            cloudwatch.put_metric_alarm(
                AlarmName='ELB Latency is High on %s' % elb,
                ComparisonOperator='GreaterThanThreshold',
                EvaluationPeriods=1,
                MetricName='Latency',
                Namespace='AWS/ELB',
                Period=60,
                Statistic='Average',
                Threshold=40.0,
                ActionsEnabled=False,
                AlarmDescription='Alarm when ELB latency Spike over 40',
                Dimensions=[
                {
                    'Name': 'ELB_Name',
                    'Value': elb
                },
                ],
                Tags=[
                {
                    'Key': 'type',
                    'Value': 'Latency'
                },
                {
                    'Key': 'Name',
                    'Value': elb
                }           
                ],
                Unit='Seconds'
                )
            print("Latency Monitor Successfully created for :", elb)
    print("==========================================")

def Create_ELB_RequestCount(elb_list):
    for alarm_iterator in monitor.alarms.all():
        Cloudwatch_Monitor_List.append(alarm_iterator.name)

    Monitor_List = str(Cloudwatch_Monitor_List)
    for elb in elb_list: 
        if list(set(re.findall(r'requestcount is high on*(?: *([\w.-]+))?', Monitor_List.lower()))):
            print('RequestCount Alarm is Present for :', elb)
            
        else:
            cloudwatch.put_metric_alarm(
                AlarmName='RequestCount is High on %s' % elb,
                ComparisonOperator='GreaterThanThreshold',
                EvaluationPeriods=1,
                MetricName='RequestCount',
                Namespace='AWS/ELB',
                Period=60,
                Statistic='Average',
                Threshold=40.0,
                ActionsEnabled=False,
                AlarmDescription='Alarm when RequestCount Spike over 40',
                Dimensions=[
                {
                    'Name': 'ELB_Name',
                    'Value': elb
                },
                ],
                Tags=[
                {
                    'Key': 'type',
                    'Value': 'RequestCount'
                },
                {
                    'Key': 'Name',
                    'Value': elb
                }           
                ],
                Unit='Seconds'
                )
            print("RequestCount Monitor Successfully created for :", elb)
    print("==========================================")

def Create_ELB_UnHealthyHostCount(elb_list):
    for alarm_iterator in monitor.alarms.all():
        Cloudwatch_Monitor_List.append(alarm_iterator.name)

    Monitor_List = str(Cloudwatch_Monitor_List)
    for elb in elb_list: 
        if list(set(re.findall(r'unhealthyHostCount is high on*(?: *([\w.-]+))?', Monitor_List.lower()))):
            print('RequestCount Alarm is Present for :', elb)
            
        else:
            cloudwatch.put_metric_alarm(
                AlarmName='UnHealthyHostCount is High on %s' % elb,
                ComparisonOperator='GreaterThanThreshold',
                EvaluationPeriods=1,
                MetricName='UnHealthyHostCount',
                Namespace='AWS/ELB',
                Period=60,
                Statistic='Average',
                Threshold=1,
                ActionsEnabled=False,
                AlarmDescription='Alarm when UnHealthyHostCount Spike over 1',
                Dimensions=[
                {
                    'Name': 'ELB_Name',
                    'Value': elb
                },
                ],
                Tags=[
                {
                    'Key': 'type',
                    'Value': 'UnHealthyHostCount'
                },
                {
                    'Key': 'Name',
                    'Value': elb
                }           
                ],
                Unit='Seconds'
                )
            print("UnHealthyHostCount Monitor Successfully created for :", elb)
    print("==========================================")
