import requests
import random


with open('valid_proxies.txt', 'r') as f:
    ip_addresses  = f.read().split("\n")
website = 'https://toscrape.com/'

def proxy_request(website):
   valid_proxy_list = []
   i = 0
   for i in ip_addresses:
      try:
        r = requests.get(website, proxies={'http':i, 'https':i}, timeout=1)
        if r.status_code == 200:
            valid_proxy_list.append(i)
        print(i)
      except Exception as err:
        pass
   return valid_proxy_list

out = proxy_request(website)

print(out)

with open("valid_proxies.txt", "w") as file:
   file.write(str((proxy_request(website))))
   
