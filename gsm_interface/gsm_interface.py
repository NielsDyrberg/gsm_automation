
"""
This interface should enable and ease up the use of the hw GSM module
"""

"""
Remember to activate hw serial on RPI
    1. raspi-config
        a. 5. Interface options
        b. P6 Serial
        c. No to login over serial
        d. Yes to enable hw serial
    2. Find uart mapping using "ls -l /dev"
        You are looking for "serial0 -> ttyS0" and "serial1 -> ttyAMA0"
"""

import serial
from time import sleep

class GSMInterface:
    def __init__(self):
        self.ser = serial.Serial("/dev/ttyS0", 9600)  # Open port with baud rate

    def send_cmd(self):
        cmd = b"AT+CMGF=1\n"
        print(cmd)
        self.ser.write(cmd)  #Set in Text mode
        sleep(0.3)
        response = self.ser.readline()
        print(response)
        sleep(0.200)

        cmd = b"AT+CMGS=\"20405458\"\r\n"
        print(cmd)
        self.ser.write(cmd)  # Set in Text mode
        sleep(0.3)
        response = self.ser.readline()
        print(response)
        response = self.ser.readline()
        print(response)
        sleep(0.200)

        cmd = b"Fra Pi\n"
        print(cmd)
        self.ser.write(cmd)  # Set in Text mode
        sleep(0.3)
        response = self.ser.readline()
        print(response)

        cmd = b"\x1A\n"
        print(cmd)
        self.ser.write(cmd)  # Set in Text mode
        sleep(0.3)
        response = self.ser.readline()
        print(response)
        response = self.ser.readline()
        print(response)
        sleep(0.500)
        while self.ser.in_waiting:
            print(self.ser.readline())
            print(self.ser.readline())
            sleep(0.400)