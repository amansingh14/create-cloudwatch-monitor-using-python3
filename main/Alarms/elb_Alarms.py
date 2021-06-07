
## This file has following functions:
# 1. Create_ELB_Latency(dict elb_list)
# 2. Create_ELB_RequestCount(dict elb_list)
# 3. Create_ELB_UnHealthyHostCount(dict elb_list)
# 4. Create_ELB_HTTPCode_ELB_5XX(dict elb_list)

####

import boto3
from Variable import ELB_Alarm_Params
import re
monitor                    = boto3.resource('cloudwatch')
cloudwatch                 = boto3.client('cloudwatch')
Var_ELB_Latency            = ELB_Alarm_Params.ELB_Latency_Variable
Var_ELB_RequestCount       = ELB_Alarm_Params.ELB_RequestCount_Variable
Var_ELB_UnhealthyhostCount = ELB_Alarm_Params.ELB_UnhealthyhostCount_Variable
Var_ELB_5XX                = ELB_Alarm_Params.ELB_5XX_Variable


Cloudwatch_Monitor_List = []

# function to create Latency Alarm.

def Create_ELB_Latency(elb_list):
    for alarm_iterator in monitor.alarms.all():
        Cloudwatch_Monitor_List.append(alarm_iterator.name)

    Monitor_List = str(Cloudwatch_Monitor_List)
    for elb in elb_list: 
        if list(set(re.findall(r'elb : latency is high on*(?: *([\w.-]+))?', Monitor_List.lower()))):
            print('ELB Latency Alarm is Present for :', elb)
            
        else:
            cloudwatch.put_metric_alarm(
                AlarmName           = Var_ELB_Latency.AlarmName + '%s' % elb,
                AlarmDescription    = Var_ELB_Latency.AlarmDescription,
                ComparisonOperator  = Var_ELB_Latency.ComparisonOperator,
                EvaluationPeriods   = Var_ELB_Latency.EvaluationPeriods,
                MetricName          = Var_ELB_Latency.MetricName,
                Namespace           = Var_ELB_Latency.Namespace,
                Period              = Var_ELB_Latency.Period,
                Statistic           = Var_ELB_Latency.Statistic,
                Threshold           = Var_ELB_Latency.Threshold,
                Unit                = Var_ELB_Latency.Unit,
                TreatMissingData    = Var_ELB_Latency.TreatMissingData,
                ActionsEnabled      = Var_ELB_Latency.ActionsEnabled,
                OKActions = [
                    Var_ELB_Latency.OKActions,
                ],
                AlarmActions = [
                    Var_ELB_Latency.AlarmActions,
                ],
                Dimensions=[
                {
                    'Name': Var_ELB_Latency.Dimensions_Name,
                    'Value': elb
                },
                ],
                Tags=[
                {
                    'Key': Var_ELB_Latency.Tags_Key,
                    'Value': Var_ELB_Latency.Tags_Value
                },
                          
                ]
                
                )
            print("Latency Monitor Successfully created for :", elb)
    print("==========================================")

# function to create requestcount Alarm

def Create_ELB_RequestCount(elb_list):
    for alarm_iterator in monitor.alarms.all():
        Cloudwatch_Monitor_List.append(alarm_iterator.name)

    Monitor_List = str(Cloudwatch_Monitor_List)
    for elb in elb_list: 
        if list(set(re.findall(r'requestcount is high on*(?: *([\w.-]+))?', Monitor_List.lower()))):
            print('RequestCount Alarm is Present for :', elb)
            
        else:
            cloudwatch.put_metric_alarm(
                AlarmName           = Var_ELB_RequestCount.AlarmName + '%s' % elb,
                AlarmDescription    = Var_ELB_RequestCount.AlarmDescription,
                ComparisonOperator  = Var_ELB_RequestCount.ComparisonOperator,
                EvaluationPeriods   = Var_ELB_RequestCount.EvaluationPeriods,
                MetricName          = Var_ELB_RequestCount.MetricName,
                Namespace           = Var_ELB_RequestCount.Namespace,
                Period              = Var_ELB_RequestCount.Period,
                Statistic           = Var_ELB_RequestCount.Statistic,
                Threshold           = Var_ELB_RequestCount.Threshold,
                Unit                = Var_ELB_RequestCount.Unit,
                TreatMissingData    = Var_ELB_RequestCount.TreatMissingData,
                ActionsEnabled      = Var_ELB_RequestCount.ActionsEnabled,
                OKActions = [
                    Var_ELB_RequestCount.OKActions,
                ],
                AlarmActions = [
                    Var_ELB_RequestCount.AlarmActions,
                ],
                Dimensions=[
                {
                    'Name': Var_ELB_RequestCount.Dimensions_Name,
                    'Value': elb
                },
                ],
                Tags=[
                {
                    'Key': Var_ELB_RequestCount.Tags_Key,
                    'Value': Var_ELB_RequestCount.Tags_Value
                },
                          
                ]
                
                )
            print("RequestCount Monitor Successfully created for :", elb)
    print("==========================================")

# function to create UnhealthyhostCount alarm
def Create_ELB_UnHealthyHostCount(elb_list):
    for alarm_iterator in monitor.alarms.all():
        Cloudwatch_Monitor_List.append(alarm_iterator.name)

    Monitor_List = str(Cloudwatch_Monitor_List)
    for elb in elb_list: 
        if list(set(re.findall(r'unhealthyHostCount is high on*(?: *([\w.-]+))?', Monitor_List.lower()))):
            print('RequestCount Alarm is Present for :', elb)
            
        else:
            cloudwatch.put_metric_alarm(
                AlarmName           = Var_ELB_UnhealthyhostCount.AlarmName + '%s' % elb,
                AlarmDescription    = Var_ELB_UnhealthyhostCount.AlarmDescription,
                ComparisonOperator  = Var_ELB_UnhealthyhostCount.ComparisonOperator,
                EvaluationPeriods   = Var_ELB_UnhealthyhostCount.EvaluationPeriods,
                MetricName          = Var_ELB_UnhealthyhostCount.MetricName,
                Namespace           = Var_ELB_UnhealthyhostCount.Namespace,
                Period              = Var_ELB_UnhealthyhostCount.Period,
                Statistic           = Var_ELB_UnhealthyhostCount.Statistic,
                Threshold           = Var_ELB_UnhealthyhostCount.Threshold,
                Unit                = Var_ELB_UnhealthyhostCount.Unit,
                TreatMissingData    = Var_ELB_UnhealthyhostCount.TreatMissingData,
                ActionsEnabled      = Var_ELB_UnhealthyhostCount.ActionsEnabled,
                OKActions = [
                    Var_ELB_UnhealthyhostCount.OKActions,
                ],
                AlarmActions = [
                    Var_ELB_UnhealthyhostCount.AlarmActions,
                ],
                Dimensions=[
                {
                    'Name': Var_ELB_UnhealthyhostCount.Dimensions_Name,
                    'Value': elb
                },
                ],
                Tags=[
                {
                    'Key': Var_ELB_UnhealthyhostCount.Tags_Key,
                    'Value': Var_ELB_UnhealthyhostCount.Tags_Value
                },
                          
                ]
                
                )
            print("UnHealthyHostCount Monitor Successfully created for :", elb)
    print("==========================================")

# function to create 5xx error count alarm
def Create_ELB_HTTPCode_ELB_5XX(elb_list):
    for alarm_iterator in monitor.alarms.all():
        Cloudwatch_Monitor_List.append(alarm_iterator.name)

    Monitor_List = str(Cloudwatch_Monitor_List)
    for elb in elb_list: 
        if list(set(re.findall(r'5xx error count is high on*(?: *([\w.-]+))?', Monitor_List.lower()))):
            print('RequestCount Alarm is Present for :', elb)
            
        else:
            cloudwatch.put_metric_alarm(
                AlarmName           = Var_ELB_5XX.AlarmName + '%s' % elb,
                AlarmDescription    = Var_ELB_5XX.AlarmDescription,
                ComparisonOperator  = Var_ELB_5XX.ComparisonOperator,
                EvaluationPeriods   = Var_ELB_5XX.EvaluationPeriods,
                MetricName          = Var_ELB_5XX.MetricName,
                Namespace           = Var_ELB_5XX.Namespace,
                Period              = Var_ELB_5XX.Period,
                Statistic           = Var_ELB_5XX.Statistic,
                Threshold           = Var_ELB_5XX.Threshold,
                Unit                = Var_ELB_5XX.Unit,
                TreatMissingData    = Var_ELB_5XX.TreatMissingData,
                ActionsEnabled      = Var_ELB_5XX.ActionsEnabled,
                OKActions = [
                    Var_ELB_5XX.OKActions,
                ],
                AlarmActions = [
                    Var_ELB_5XX.AlarmActions,
                ],
                Dimensions=[
                {
                    'Name': Var_ELB_5XX.Dimensions_Name,
                    'Value': elb
                },
                ],
                Tags=[
                {
                    'Key': Var_ELB_5XX.Tags_Key,
                    'Value': Var_ELB_5XX.Tags_Value
                },
                          
                ]
                
                )
            print("5XX error count Monitor Successfully created for :", elb)
    print("==========================================")
