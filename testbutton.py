import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.IN)
def printo(ara):
    print('ok')

GPIO.add_event_detect(22,GPIO.BOTH,printo)
while True:pass
