# -*- coding: utf-8 -*-
import rangefinder
import RPi.GPIO as GPIO
import gps
import request
from threading import Thread
import time
ALERT_DISTANCE = 45
GPIO.setup(22,GPIO.IN)
isDelayHelpRequest = False
print('starting with alert distance ',ALERT_DISTANCE,'cm')
def sentHelpRequest(arg=None):
    global isDelayHelpRequest
    isDelayHelpRequest = True
    request.sentMessage(str('Need Help!\n')+request.getGoogleMapLink(gps.getLastLatLng()))
    print('sent help request')
    time.sleep(4)
    isDelayHelpRequest = False
def makeRequest(arg=None):
    if not isDelayHelpRequest:
        t = Thread(target=sentHelpRequest)
        t.daemon = True
        t.start()
if __name__ == '__main__':
    gps.startWithThread()
    GPIO.add_event_detect(22,GPIO.BOTH,makeRequest)
    while True:
        distance = rangefinder.getDistance()
        print('distance ',distance,'cm')
        if distance < ALERT_DISTANCE:
            rangefinder.beep(0.25)
            print('FOUNDED')
        
