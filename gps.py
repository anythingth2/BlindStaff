import serial
import pynmea2
import time
from threading import Thread
PORT = '/dev/ttyAMA0'
port = serial.Serial(PORT,9600,timeout=2)
msg = '\n'
lastLatLng = ()
with open('gps_log.txt','r') as f:
    lastLatLng = [float(x) for x in f.readline().split(' ')]

# log = open('gps_log.txt','w')
def getLastLatLng():
    return lastLatLng

def start():
    while True:
        while not port.readable():
            try:
                port.open()
            except:
                print('trying to open port that already opened')
        msg = ''
        while msg == '' :
            try:
                #time.sleep(0.1)
                msg = pynmea2.parse(port.readline())
                # log.write(str(msg)+'\n')
                #if msg in [pynmea2.RMC,pynmea2.GGA,pynmea2.GLL]:
                #    break
            except:
                msg = ''
                time.sleep(0.1)
                #print('failed to read gps')
        if type(msg) in [pynmea2.RMC,pynmea2.GGA,pynmea2.GLL]:
            if msg.lat != '' and msg.lon != '':
                lastLatLng = (float(msg.lat)/100,float(msg.lon)/100)
                open('gps_log.txt','w').write(str(lastLatLng[0]),str(lastLatLng[1]))
        time.sleep(0.25)


def startWithThread():
    t = Thread(target=start)
    t.daemon = on 
    t.start()