import serial

import pynmea2
import time
PORT = '/dev/ttyAMA0'
port = serial.Serial(PORT,9600,timeout=2)
msg = '\n'
log = open('gps_log.txt','w')
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
            log.write(str(msg)+'\n')
            #if msg in [pynmea2.RMC,pynmea2.GGA,pynmea2.GLL]:
            #    break
        except:
            msg = ''
            time.sleep(0.1)
            #print('failed to read gps')
    if type(msg) in [pynmea2.RMC,pynmea2.GGA,pynmea2.GLL]:
        print(type(msg),msg)
    #print(dir(msg))
    #print(msg.lat,msg.lon)
    time.sleep(0.25)
