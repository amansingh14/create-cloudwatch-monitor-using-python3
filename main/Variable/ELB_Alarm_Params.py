# Author : Aman Singh
# Org : nClouds Inc.

# Refer https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html for documentation.
# Use this variable file to set variables for monitors
#################################################################
#       VAIRABLES               Expected values                 #
#################################################################
#    AlarmName              =   <String>
#    ActionsEnabled         =   True | False                 <boolean>
#    OKActions              =   'arn:aws:sns:us-east-1:695292474035:test-automation-cloudwatch' <String>
#    AlarmActions           =   SNS notification channel      <String>
#    MetricName             =   Metric <String>
#    Namespace              =   'AWS/ELB'
#    Statistic              =   'SampleCount' | 'Average' | 'Sum' | 'Minimum' | 'Maximum' , 
#    Period                 =   Value in Seconds
#    Unit                   =   'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
#    EvaluationPeriods      =   <int>
#    DatapointsToAlarm      =   <int>
#    Threshold              =   <int>
#    ComparisonOperator     =   'GreaterThanOrEqualToThreshold'|'GreaterThanThreshold'|'LessThanThreshold'|'LessThanOrEqualToThreshold'|'LessThanLowerOrGreaterThanUpperThreshold'|'LessThanLowerThreshold'|'GreaterThanUpperThreshold',
#    TreatMissingData       =   'breaching' | 'notBreaching' | 'ignore' | 'missing'
#    Tags_Key               =   <String>
#   Tags_Value              =   <String>
#    AlarmDescription       =   <String>
#    Dimensions_Name        =   <String>                                       
#            
##########################################################################
##########################################################################
######             Variable for ELB Alarms                          ######
##########################################################################
##########################################################################

class ELB_Latency_Variable:

    AlarmName              = 'ELB : Latency is High on '
    ActionsEnabled         =  True                                                            
    OKActions              = 'arn:aws:sns:us-east-1:695292474035:test-automation-cloudwatch'
    AlarmActions           = 'arn:aws:sns:us-east-1:695292474035:test-automation-cloudwatch'  
    MetricName             = 'Latency'
    Namespace              = 'AWS/ELB'
    Statistic              = 'Average'                                                        
    Period                 = 60
    Unit                   = 'Seconds'                                                                
    EvaluationPeriods      = 1
    DatapointsToAlarm      = 1
    Threshold              = 10.0
    ComparisonOperator     = 'GreaterThanOrEqualToThreshold'                                 
    TreatMissingData       = 'missing'
    Tags_Key               = 'Name'
    Tags_Value             = 'ELB_Latency'
    AlarmDescription       = 'Alarm when ELB latency Spike over ' + str(Threshold)
    Dimensions_Name        = 'LoadBalancerName'

class ELB_RequestCount_Variable:

    AlarmName              = 'ELB : RequestCount is High on '
    ActionsEnabled         =  True                                                           
    OKActions              = 'arn:aws:sns:us-east-1:695292474035:test-automation-cloudwatch'
    AlarmActions           = 'arn:aws:sns:us-east-1:695292474035:test-automation-cloudwatch' 
    MetricName             = 'RequestCount'
    Namespace              = 'AWS/ELB'
    Statistic              = 'Average'                                                        
    Period                 = 60
    Unit                   = 'Count'             
    EvaluationPeriods      = 1
    DatapointsToAlarm      = 1
    Threshold              = 10.0
    ComparisonOperator     = 'GreaterThanOrEqualToThreshold'                                 
    TreatMissingData       = 'missing'
    Tags_Key               = 'Name'
    Tags_Value             = 'ELB_RequestCount'
    AlarmDescription       = 'Alarm when ELB RequestCount Spike over ' + str(Threshold)
    Dimensions_Name        = 'LoadBalancerName'

class ELB_UnhealthyhostCount_Variable:

    AlarmName              = 'ELB : UnhealthyHostCount is Greater than One '
    ActionsEnabled         =  True                                                           
    OKActions              = 'arn:aws:sns:us-east-1:695292474035:test-automation-cloudwatch'
    AlarmActions           = 'arn:aws:sns:us-east-1:695292474035:test-automation-cloudwatch' 
    MetricName             = 'RequestCount'
    Namespace              = 'AWS/ELB'
    Statistic              = 'Average'                                                        
    Period                 = 60
    Unit                   = 'Count'             
    EvaluationPeriods      = 1
    DatapointsToAlarm      = 1
    Threshold              = 1.0
    ComparisonOperator     = 'GreaterThanOrEqualToThreshold'                                 
    TreatMissingData       = 'missing'
    Tags_Key               = 'Name'
    Tags_Value             = 'ELB_RequestCount'
    Dimensions_Name        = 'LoadBalancerName'
    AlarmDescription       = 'Alarm when ELB UnhealthyHostCount Greater than ' + str(Threshold)

class ELB_5XX_Variable:

    AlarmName              = 'ELB : 5XX error count is High on '
    ActionsEnabled         =  True                                                           
    OKActions              = 'arn:aws:sns:us-east-1:695292474035:test-automation-cloudwatch'
    AlarmActions           = 'arn:aws:sns:us-east-1:695292474035:test-automation-cloudwatch' 
    MetricName             = 'RequestCount'
    Namespace              = 'AWS/ELB'
    Statistic              = 'Average'                                                        
    Period                 = 60
    Unit                   = 'Count'             
    EvaluationPeriods      = 1
    DatapointsToAlarm      = 1
    Threshold              = 20
    ComparisonOperator     = 'GreaterThanOrEqualToThreshold'                                 
    TreatMissingData       = 'missing'
    Tags_Key               = 'Name'
    Tags_Value             = 'ELB_RequestCount'
    Dimensions_Name        = 'LoadBalancerName'
    AlarmDescription       = 'Alarm when ELB 5XX error count Spike over ' + str(Threshold)
    
    
        
       
