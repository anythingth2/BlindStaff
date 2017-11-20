import RPi.GPIO as GPIO
import time
#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
alertDistance = 45
trigPin = 17
echoPin = 27
buzzerPin = 4
GPIO.setup(18,GPIO.OUT)
buzzerPWM = GPIO.PWM(18,250)
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
    buzzerPWM.start(0.75)
    time.sleep(t)
    buzzerPWM.stop()
    GPIO.output(buzzerPin,GPIO.HIGH)
        
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
    if distance < alertDistance:
        beep(0.25)
        print('FOUNDED!','Distance :',distance,'cm')
    else: print('Distance :',distance,'cm')
    #print(GPIO.input(echoPin))
    time.sleep(0.1)
GPIO.cleanup()
