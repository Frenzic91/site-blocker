from time import *
from datetime import datetime as dt

hosts_path = '/mnt/c/Windows/System32/drivers/etc/hosts'
redirect_ip = '127.0.0.1'
website_list = ['www.youtube.com', 'youtube.com']

while True:
    now = dt.now()
    if dt(now.year, now.month, now.day, 0) < now < dt(now.year, now.month, now.day, 1):
        print('Websites are being blocked')
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect_ip + ' ' + website + '\n')
    else:
        print('All websites are available')
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
               if not any(website in line for website in website_list):
                   file.write(line)
            file.truncate()
    sleep(5)
