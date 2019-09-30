import os
import re
from subprocess import check_output
import time

response = check_output(["speedtest-cli", "--simple"]).decode("utf-8")

ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

ping[0] = ping[0].replace(',', '.')
download[0] = download[0].replace(',', '.')
upload[0] = upload[0].replace(',', '.')

try:
    if os.stat('speedtest.csv').st_size == 0:
        print('Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)')
except:
    pass

print('{},{},{},{},{}'.format(time.strftime('%Y-%m-%d'), time.strftime('%H:%M'), ping[0], download[0], upload[0]))