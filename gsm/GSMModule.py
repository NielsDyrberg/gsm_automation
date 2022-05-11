
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

"""
Todo list:
"""
#TODO: Add method add_number
#TODO: Save numbers in a hashed file
#TODO: Refactor use of AT conmmands

import serial
from time import sleep
import executers

class GSMModule:
    execute = executers.ExecutionHandler()
    ser = serial.Serial("/dev/ttyS0", 9600)  # Open port with baud rate'

    def __init__(self, contact_number):
        if contact_number is not None:
            self.contact_number = contact_number
        else:
            raise ValueError("Contact number can't be None")

    def _clean_reply(self, _reply):
        """
        Removes GSM junk from received message
        :param _reply: The message to clean
        :return: The cleaned msg
        """
        #fixme: make a generic msg cleaner
        cleaned_reply = ""
        reply = str(_reply).lower()
        if "ok" in reply:
            return "ok"
        elif "diesel" in reply:
            return "diesel"
        return cleaned_reply

    def assert_ok(self, message):
        ret_value = b"OK" in message
        if ret_value:
            print("Msg: OK")
        else:
            print("Msg: Not OK")
        return ret_value

    def is_ready(self):
        # Resetting to defaults
        cmd = b"ATZ\r"
        print("Cmd: " + str(cmd))
        self.ser.write(cmd)
        sleep(2)
        reply = self.ser.read(self.ser.inWaiting())
        return self.assert_ok(reply)

    def send_sms(self, message_to_send):
        cmd = b"AT+CMGF=1\r"
        print("Sending: " + str(cmd))
        self.ser.write(cmd)  #Set in Text mode
        sleep(0.3)
        reply = self.ser.read(self.ser.inWaiting())
        sleep(0.200)

        cmd = b"AT+CMGS=\"" + bytes(self.contact_number, "utf-8") + b"\"\r"
        print(cmd)
        self.ser.write(cmd)  # Set in Text mode
        sleep(0.3)
        reply = self.ser.read(self.ser.inWaiting())
        print(reply)
        sleep(0.200)

        cmd = bytes(message_to_send, "utf-8") + b"\r"
        print(cmd)
        self.ser.write(cmd)  # Set in Text mode
        sleep(0.3)
        reply = self.ser.read(self.ser.inWaiting())
        print(reply)

        cmd = b"\x1A\r"
        print(cmd)
        self.ser.write(cmd)  # Set in Text mode
        sleep(0.3)
        reply = self.ser.read(self.ser.inWaiting())
        print(reply)
        sleep(0.500)
        while self.ser.in_waiting:
            print(self.ser.readline())
            print(self.ser.readline())
            sleep(0.400)

    def receive_msg(self):
        self.ser.write(b"AT+CMGF=1\r")  # set to text mode
        sleep(3)
        self.ser.write(b'AT+CMGDA="DEL ALL"\r')  # delete all SMS
        sleep(3)
        _ = self.ser.read(self.ser.inWaiting())  # Clean buffer
        print("Listening for incomming SMS...")
        while True:
            reply = self.ser.read(self.ser.inWaiting())
            if reply != b"":
                self.ser.write(b"AT+CMGR=1\r")
                sleep(3)
                reply = self.ser.read(self.ser.inWaiting())
                print("SMS received. Content:")
                print(reply)
                reply = self._clean_reply(reply)
                self.execute.handler(reply)
                sleep(3)
                self.ser.write(b'AT+CMGDA="DEL ALL"\r')  # delete all
                sleep(3)
                self.ser.read(self.ser.inWaiting())  # Clear buf
            sleep(5)