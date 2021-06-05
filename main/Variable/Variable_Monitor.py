# Author : Aman Singh
# Org : nClouds Inc.

# Refer https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html for documentation.
# Use this variable file to set variables for monitors
                                        
            
##########################################################################
##########################################################################
######             Variable for ELB Alarms                          ######
##########################################################################
##########################################################################

class ELB_Latency_Variable:

    AlarmName              = 'ELB : Latency is High on'
    ActionsEnabled         =  True                                                           # True | False 
    OKActions              = 'arn:aws:sns:us-east-1:695292474035:test-automation-cloudwatch'
    AlarmActions           = 'arn:aws:sns:us-east-1:695292474035:test-automation-cloudwatch'  # SNS notification 
    MetricName             = 'Latency'
    Namespace              = 'AWS/ELB'
    Statistic              = 'Average'                                                        #'SampleCount' | 'Average' | 'Sum' | 'Minimum' | 'Maximum' , 
    Period                 = 60
    Unit                   = 'Seconds'                                                                # 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
    EvaluationPeriods      = 1
    DatapointsToAlarm      = 1
    Threshold              = 10.0
    ComparisonOperator     = 'GreaterThanOrEqualToThreshold'                                 #'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold'|'LessThanLowerOrGreaterThanUpperThreshold'|'LessThanLowerThreshold'|'GreaterThanUpperThreshold',
    TreatMissingData       = 'missing'
    Tags_Key               = 'Name'
    Tags_Value            = 'ELB_Latency'
    AlarmDescription       = 'Alarm when ELB latency Spike over ' + str(Threshold)
    Dimensions_Name        = 'LoadBalancerName'
    
    
        
       
