from time import *
from datetime import datetime as dt

host_path = r'C:\Windows\System32\drivers\etc\hosts'
redirect_ip = '127.0.0.1'
websites = ['www.youtube.com', 'youtube.com']

while True:
    now = dt.now()
    if dt(now.year, now.month, now.day, 8) < now < dt(now.year, now.month, now.day, 16):
        print('Websites are being blocked')
    else:
        print('All websites are available')

    sleep(5)
