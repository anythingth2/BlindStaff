# -*- coding: utf-8 -*-
import rangefinder
import RPi.GPIO as GPIO
import gps
import request

ALERT_DISTANCE = 45
print('starting with alert distance ',ALERT_DISTANCE,'cm')
def sentHelpRequest():
    request.sentMessage(str('ตองการความชวยเหลอดวน!!!\n')+request.getGoogleMapLink(gps.getLastLatLng()))
    print('sent help request')

if __name__ == '__main__':
    gps.startWithThread()
    while True:
        distance = rangefinder.getDistance()
        print('distance ',distance,'cm')
        if distance < ALERT_DISTANCE:
            rangefinder.beep(0.25)
            print('FOUNDED')
        
