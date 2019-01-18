#!/usr/bin/env python3
import requests, json
from time import sleep


emailList = ['test@test.com', 'test2@test.com']

headers = {
    'User-Agent': 'HIBP Account Monitoring'
}
for email in emailList:
    URL = "https://haveibeenpwned.com/api/v2/breachedaccount/%s" %(email)
    sleep(2)
    r = requests.get(URL, headers=headers)

    if r.status_code == 404:
        print("Not pwned")
    else:
        print(r.status_code)
    #print(r.text)



