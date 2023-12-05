import requests
import re
import datetime
import time

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
toMB = lambda s : (1024*float(s[0:-2])) if s.find('G')!=-1 else float(s[0:-2])
patterns = [r"(?<=已使用 \()(.+)(?=\))", r"(?<=上传 \()(.+)(?=\))", r"(?<=下载 \()(.+)(?=\))"]
matches = []
for pat in patterns:
    match = re.search(pat, cnt)
    if match:
        matches.append(toMB(match.group()))
    else:
        print("No match")

# write csv
file = open("YourPath/VPNinfo.csv", 'a')
file.write(datetime.datetime.now().strftime('%Y/%m/%d %H:%M'))  # time for human reading
file.write(',' + str(int(time.time())))  # timestamp
for i in matches:
    file.write(',' + str(i))
file.write('\n')
file.close()

# # comparison - quicker
# old = [0.0, 0.0, 0.0]
# old[0] = quicker.context.GetVarValue('used')
# old[1] = quicker.context.GetVarValue('upload')
# old[2] = quicker.context.GetVarValue('download')

# quicker.context.SetVarValue('used', matches[0])
# quicker.context.SetVarValue('upload', matches[1])
# quicker.context.SetVarValue('download', matches[2])

# warning = 'none'
# if (matches[0] - old[0] >= 1000):
#     warning = 'Last hour used more than 1000MB.'
# if (matches[1] - matches[1] >= 1000):
#     warning = 'Abnormal Upload amount.'
# quicker.context.SetVarValue('warning', warning)
