import RPi.GPIO as GPIO
import time
#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
alertDistance = 45
trigPin = 17
echoPin = 27
buzzerPin = 4

GPIO.setup(trigPin,GPIO.OUT)
GPIO.setup(echoPin,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(buzzerPin,GPIO.OUT)
def pulseIn(pin):
    while GPIO.input(pin) == 0:
        pulsestart = time.time()
    while GPIO.input(pin) == 1:
        pulseend = time.time()
    return (pulseend - pulsestart)
def beep(t):
    GPIO.output(buzzerPin,GPIO.HIGH)
    GPIO.output(buzzerPin,GPIO.LOW)
    time.sleep(t)
    GPIO.output(buzzerPin,GPIO.HIGH)
        
def toDistance(t):
    return t * 340 / 2 * 100
    
def getDistance():
    GPIO.output(trigPin,GPIO.LOW)
    time.sleep(2*(10**-6))

    GPIO.output(trigPin,GPIO.HIGH)
    time.sleep(50*(10**-6))
    GPIO.output(trigPin,GPIO.LOW)

    duration = pulseIn(echoPin)
    distance = toDistance(duration)
    return distance
if __name__ == '__main__':
    while True:
        #GPIO.output(trigPin,GPIO.LOW)
        #time.sleep(2*(10**-6))

        #GPIO.output(trigPin,GPIO.HIGH)
        #time.sleep(50*(10**-6))
        #GPIO.output(trigPin,GPIO.LOW)
    
        #duration = pulseIn(echoPin)
        distance = getDistance() 
        if distance < 45:
            beep(0.25)
            print('FOUNDED!','Distance :',distance,'cm')
        else: print('Distance :',distance,'cm')
        #print(GPIO.input(echoPin))
        time.sleep(0.1)
GPIO.cleanup()
