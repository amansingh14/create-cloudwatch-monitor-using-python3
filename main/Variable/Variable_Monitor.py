# Author : Aman Singh
# Org : nClouds Inc.

# Refer https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html for documentation.
# Use this variable file to set variables for monitors
                                                #Possible Values
AlarmNamePrefix     = 'Lambda: Error Count is HIGH on function:'
MonitorName         =   ''
ActionsEnabled      =  'False'                  # True|False                               
Namespace           =  'AWS/EC2'                # AWS/EC2,
Period              =  '300'                    # in seconds
Statistic           =  'Average'                # 'SampleCount'|'Average'|'Sum'|'Minimum'|'Maximum'
Unit                =  'Seconds'                # 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None',
EvaluationPeriods   
DatapointsToAlarm   = '1'                           
Threshold           =  '80'
ComparisonOperator
TreatMissingData
StateValue                                      # 'OK'|'ALARM'|'INSUFFICIENT_DATA',

            
            