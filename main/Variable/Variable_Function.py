# Author : Aman Singh
# Org : nClouds Inc.


# This File to help you setting parameters for the monitor function you want to create.
#
#

####################################################
#                                                  #
#    Set Function Variablefor EC2 instance         # 
#                                                  #
####################################################

ec2_CPU_Monitor                      =   False
ec2_DiskReadOps_Monitor              =   False
ec2_DiskWriteOps_Monitor             =   False
ec2_CPUCreditUsage_Monitor           =   False

####################################################
#                                                  #
#     Set  Function variable for ELB Monitors      # 
#                                                  #
####################################################

ELB_Latency                         =  True
ELB_RequestCount                    =  True
ELB_UnHealthyHostCount              =  True
ELB_HTTPCode_ELB_5XX                =  False