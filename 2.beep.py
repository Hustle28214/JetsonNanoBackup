#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python3
#coding=utf-8
import time
from Arm_Lib import Arm_Device

# Gets the object of the manipulator
# 获取机械臂的对象
Arm = Arm_Device()
time.sleep(.1)


# In[2]:


# The buzzer will automatically sound and turn off after 100 milliseconds
# 蜂鸣器自动响100毫秒后关闭
b_time = 1
Arm.Arm_Buzzer_On(b_time)
time.sleep(1)


# In[3]:


# The buzzer will automatically sound and turn off after 300 milliseconds
# 蜂鸣器自动响300毫秒后关闭
b_time = 3
Arm.Arm_Buzzer_On(b_time)
time.sleep(1)


# In[4]:


# The buzzer keeps ringing
# 蜂鸣器一直响
Arm.Arm_Buzzer_On()
time.sleep(1)


# In[5]:


# Turn off the buzzer
# 关闭蜂鸣器
Arm.Arm_Buzzer_Off()
time.sleep(1)


# In[6]:


# Release arm object 
# 释放Arm对象
del Arm  


# In[ ]:




