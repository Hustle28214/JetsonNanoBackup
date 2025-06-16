
import time
from Arm_Lib import Arm_Device
import serial


ser = serial.Serial('/dev/ttyACM2',9600,timeout=1)

# Gets the object of the manipulator
# 获取机械臂的对象
Arm = Arm_Device()
time.sleep(.1)

while True:
    count = ser.inWaiting()
    if count != 0:
        print(ser.read(3),end='\n')
