#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python3
#coding=utf-8
import time
from Arm_Lib import Arm_Device
import  serial
import threading

ser = serial.Serial('/dev/ttyACM2',9600,timeout=1)
Arm = Arm_Device()
time.sleep(.1)


# In[2]:


def readByBytes():
    while True:
        receive = ser.readline()
        s = receive.decode()  #将ASCII方式表示的数转化为原数字对应的字符串，注意后面会有'\r\n'
        if len(s) > 5:
            print(receive, int(s[0: len(receive) - 2]))  #去掉'\r\n'并转化为整数
        else:
            print('NULL')


# In[3]:


count = ser.inWaiting()
if(b'a'==ser.read()):
    readByBytes()
                
                

