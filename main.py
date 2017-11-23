import rangefinder
import RPi.GPIO as GPIO
import gps
import request
ALERT_DISTANCE = 45

if __name__ == '__main__':
    while True:
        distance = rangefinder.getDistance()
        if distance < ALERT_DISTANCE:
            rangefinder.beep(0.25)
        elif distance < ALERT_DISTANCE + 25:
            request.sentMessage(str('ต้องการความช่วยเหลือด่วน!!!\n')+request.getGoogleMapLink(gps.getLastLatLng))
