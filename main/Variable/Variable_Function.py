
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

ELB_Latency                          =  False
ELB_RequestCount                     =  False
ELB_UnHealthyHostCount               =  False
ELB_HTTPCode_ELB_5XX                 =  False

####################################################
#                                                  #
#   Set Function variable for Lambda Monitors      # 
#                                                  #
####################################################
Lambda_Error                            = False
Lambda_Throttles                        = False
Lambda_Invocations                      = False
Lambda_ConcurrentExecutions             = False
Lambda_Duration                         = False
Lambda_UnreservedConcurrentExecutions   = False