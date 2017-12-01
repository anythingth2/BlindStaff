import rangefinder
import RPi.GPIO as GPIO
import gps
import request

ALERT_DISTANCE = 45
print('starting with alert distance ',ALERT_DISTANCE,'cm')
if __name__ == '__main__':
    gps.startWithThread()
    while True:
        distance = rangefinder.getDistance()
        print('distance ',distance,'cm')
        if distance < ALERT_DISTANCE:
            rangefinder.beep(0.25)
            print('FOUNDED')
        elif distance > ALERT_DISTANCE and distance < ALERT_DISTANCE + 25:
            request.sentMessage(str('ต้องการความช่วยเหลือด่วน!!!\n')+request.getGoogleMapLink(gps.getLastLatLng()))
            print('sent help request')
