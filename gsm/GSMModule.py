
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

from time import sleep
from .SendATCommands import SendATCommands
from .executers.ExecutionHandler import ExecutionHandler

class GSMModule:
    execute = ExecutionHandler()
    at = SendATCommands()

    def __init__(self, contact_number):
        if contact_number is not None:
            self.contact_number = contact_number
        else:
            raise ValueError("Contact number can't be None")

    def is_ready(self):
        return self.at.is_ready()

    def send_sms(self, message_to_send):
        self.at.set_to_text_mode()
        self.at.set_contact_number(self.contact_number)
        self.at.send_txt(message_to_send)
        sleep(0.500)
        self.at.read_rest()

    def receive_msg(self):
        self.at.set_to_text_mode()  # set to text mode
        sleep(3)
        self.at.delete_all_txt()
        sleep(3)
        self.at.clear_rx_buffer()
        print("Listening for incomming SMS...")
        while True:
            if self.at.in_waiting():
                reply = self.at.read_message()
                self.execute.handler(reply)
                sleep(3)
                self.at.delete_all_txt()
                sleep(3)
                self.at.clear_rx_buffer()
            sleep(5)
