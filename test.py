import serial
ser = serial.Serial('/dev/ttyACM3',9600,timeout=1)

while 1:
    if(ser.inWaiting()):
        if('a'==ser.read()):
            print('receive')

