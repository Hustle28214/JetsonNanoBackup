import serial.tools.list_ports

# 列出所有串行设备
ports = serial.tools.list_ports.comports()

# 打印每个串行设备的信息
for port in ports:
    print(port.device, port.name, port.description)
    
import serial
import re
# 打开串口连接
ser = serial.Serial('/dev/ttyACM0', 9600)  # 根据实际情况更改串口号和波特率

# 发送数据到Arduino
ser.write(b'Hello Arduino!')

# 从Arduino接收数据
received_data = ser.readline()
print("Received from Arduino:", received_data.decode())
# 关闭串口连接
ser.close()