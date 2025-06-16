import time
from Arm_Lib import Arm_Device
Arm = Arm_Device()
time.sleep(.1)



import serial
ser = serial.Serial('/dev/ttyACM1',9600,timeout=1);

while True:
    if(ser.inWaiting()):
        if('a'==ser.read):
            print('receive');
               

