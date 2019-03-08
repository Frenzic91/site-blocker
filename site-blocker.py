from time import *
from datetime import datetime as dt

hosts_temp = 'hosts'
hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect_ip = '127.0.0.1'
website_list = ['www.youtube.com', 'youtube.com']

while True:
    now = dt.now()
    if dt(now.year, now.month, now.day, 8) < now < dt(now.year, now.month, now.day, 16):
        print('Websites are being blocked')
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect_ip + ' ' + website + '\n')
    else:
        print('All websites are available')

    sleep(5)
