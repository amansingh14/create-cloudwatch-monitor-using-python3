import re
data = 'EC2 : CPU Utilization on i-0e2131e74da4fb0a2 Env: stage'
#data_2 = 'EC2 :  on i-0e2131e74da4fb0a2 Env: stage'
id_list = list(set(re.findall(r'cpu utilization on*(?: *([\w.-]+))?', str()
print(id_list)         