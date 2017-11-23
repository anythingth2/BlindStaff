# -*- coding: utf-8 -*-
import requests
import json
from threading import Thread
LINE_URL = 'https://notify-api.line.me/api/notify'
TOKEN = '12ONmCXDQ82o7J8UGb07JgbCCkY7mIGm1W8YF1pWuLH'
SELF_TOKEN = '1gGRM97rfABJ3lTWP6GKPv6IaDtWLGfRdMSzoweldm7'
header = {
    'Content-Type':'application/x-www-form-urlencoded',
    'Authorization':'Bearer '+ SELF_TOKEN
}
def getGoogleMapLink(latLng):
    return str('https://www.google.com/maps/?q=')#+str(latLng[0])+','+str(latLng[1]))

def sentMessage(text):
    body = {'message':text}
    r = requests.post(LINE_URL,body,headers=header)

if __name__ == '__main__':  
    sentMessage(str('ต้องการความช่วยเหลือด่วน!!!\n')+getGoogleMapLink((13.7288634,100.7758341)))

