import threading
import serial
import re
ser = 0



def init_serial():
    COMNUM = 3     
    global ser          #Must be declared in Each Function
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = COMNUM - 1 
    #ser.port = '/dev/ttyUSB0' #If Using Linux

    ser.timeout = 10
    ser.open()

    if ser.isOpen():
        print 'Open: ' + ser.portstr + ' at ' + str(ser.baudrate) + ' baudrate'


init_serial()



def worker():
    while 1:
        data_left = ser.inWaiting()
        if data_left > 0:
            serialmsg = ser.readline()
            print serialmsg


t = threading.Thread(target=worker)
t.start()


while 1:
    atcmd = raw_input()
    ser.write(atcmd + '\r\n')


    
