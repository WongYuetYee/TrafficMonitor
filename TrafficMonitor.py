import requests
import re
import datetime

# get contents
data = {'token': '96051eb7fd82b2c91a32ccdc4073e2381cbda956',\
        'username': 'your_own_id',\
        'password': 'your_own_password'}
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
headers = {'User-Agent': useragent}
login_url = "https://www.bmb776.com/dologin.php"
url = "https://www.bmb776.com/clientarea.php?action=productdetails&id=260483"

session = requests.Session()
session.trust_env = False
response = session.post(login_url, headers=headers, data=data)
response = session.get(url)

# save cnt
cnt = response.text
cnt = cnt.replace(',', ',\n')
cnt = cnt.replace('\u2740', ' ')

# use cnt
string = cnt
result = ''

pattern = r"已使用 \(.*?(?=\))"
match = re.search(pattern, string)
if match:
    result = result + match.group() + ')\n'
else:
    print("No match")

pattern = r"上传 \(.*?(?=\))"
match = re.search(pattern, string)
if match:
    result = result + match.group() + ')\n'
else:
    print("No match")

pattern = r"下载 \(.*?(?=\))"
match = re.search(pattern, string)
if match:
    result = result + match.group() + ')\n'
else:
    print("No match")

file = open("H:/OneDrive - mail3.sysu.edu.cn/4-Function/ToolsKit/VPNinfo.txt", 'a')
file.write(datetime.datetime.now().strftime('%Y-%m-%d  %H:%M'))
file.write('\n' + result)
file.close()

# # comparison - quicker
# pattern = r"\((.*?)\)"
# string = result
# matches = re.findall(pattern, string)
# 
# for ind, x in enumerate(matches):
#     if 'GB' in x:
#         matches[ind] = (float(x[:-3]) * 1024)
#     else:
#         matches[ind] = (float(x[:-3]))
# 
# old = [0.0, 0.0, 0.0]
# old[0] = quicker.context.GetVarValue('used')
# old[1] = quicker.context.GetVarValue('upload')
# old[2] = quicker.context.GetVarValue('download')
# 
# quicker.context.SetVarValue('used', matches[0])
# quicker.context.SetVarValue('upload', matches[1])
# quicker.context.SetVarValue('download', matches[2])
# 
# warning = 'none'
# if (matches[0] - old[0] >= 1000):
#     warning = 'Last hour used more than 1000MB.\n'
# if (matches[1] > matches[2]):
#     warning = warning + 'Abnormal Upload amount.'
# quicker.context.SetVarValue('warning', warning)
