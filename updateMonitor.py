import psutil
import requests
import time
import datetime
import platform
import os

system = platform.system()
deviceID = 3
devicePasscode = "yomama"

def main():
    while True:
        CPUUsage = psutil.cpu_percent()
        CPUCount = psutil.cpu_count()
        RAMUsagePerCent = psutil.virtual_memory().percent
        RAMTotal = psutil.virtual_memory().total >> 20
        RAMUsageValue = psutil.virtual_memory().used >> 20
        rootDiskTotal = psutil.disk_usage('/').total >> 20
        rootDiskFree = psutil.disk_usage('/').free >> 20
        rootDiskUsedPerCent = psutil.disk_usage('/').percent
        rootDiskUsedValue = psutil.disk_usage('/').used >> 20

        body = {'deviceID': deviceID, 'devicePasscode': devicePasscode, 'CPUUsage': CPUUsage, 'CPUCount': CPUCount,
                'RAMUsagePerCent': RAMUsagePerCent, 'RAMUsageValue': RAMUsageValue, 'RAMTotal': RAMTotal,
                'rootDiskTotal': rootDiskTotal, 'rootDiskFree': rootDiskFree,
                'rootDiskUsedPerCent': rootDiskUsedPerCent, 'rootDiskUsedValue': rootDiskUsedValue}
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'pythonRequests'}
        r = requests.post('https://dcsites.co.uk/devicemonitor/api/update/', data=body, headers=headers)
        # print(r.headers['content-type'])
        print(r.text)
        log(r.text)
        time.sleep(5)

def log(value):
    if system == 'Windows':
        if not os.path.isdir("C:/temp"):
            os.mkdir("C:/temp")
        file = open("C:/temp/updateMonitorLog.txt", "a")
    else:
        file = open('/tmp/updateMonitorLog.txt', "a")
    timeNow = datetime.datetime.now()
    file.write(str(timeNow) + ": " + value + "\n")
    file.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopped by CRTL + C')
        exit()
