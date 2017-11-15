import RPi.GPIO as GPIO
import time
#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

trigPin = 17
echoPin = 27
GPIO.setup(trigPin,GPIO.OUT)
GPIO.setup(echoPin,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
def pulseIn(pin):
    trig = 10**-6
    pulsestart = time.time()
    while GPIO.input(pin) == 1:pass
    pulsestart = time.time()
    while GPIO.input(pin) == 0:pass
    pulseend = time.time()
    return (pulseend - pulsestart)

        
def getDistance(t):
    
    return t * 340 / 2 * 100
while True:
    GPIO.output(trigPin,GPIO.LOW)
    time.sleep(2*(10**-6))

    GPIO.output(trigPin,GPIO.HIGH)
    time.sleep(50*(10**-6))
    GPIO.output(trigPin,GPIO.LOW)
    
    duration = pulseIn(echoPin)
    distance = getDistance(duration)
    print('Distance ',distance,'cm')
    #print(GPIO.input(echoPin))
    time.sleep(0.1)
GPIO.cleanup()
