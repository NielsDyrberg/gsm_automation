
import serial
from time import sleep


class SendATCommands:
    """
    Sends AT commands and returns the cleaned response
    """
    _ser = serial.Serial("/dev/ttyS0", 9600)  # Open port with baud rate'

    def __init__(self):
        pass

    def _send_at_cmd(self, _cmd):
        print(_cmd)
        self._ser.write(_cmd)
        sleep(0.3)
        reply = self._ser.read(self._ser.inWaiting())
        print(reply)
        sleep(0.200)
        return reply

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

    def _assert_ok(self, message):
        ret_value = b"OK" in message
        if ret_value:
            print("Msg: OK")
        else:
            print("Msg: Not OK")
        return ret_value

    def in_waiting(self):
        return self._ser.inWaiting()

    def send_txt(self, msg_to_send):
        cmd = bytes(msg_to_send, "utf-8") + b"\r" + b"\x1A\r"
        return self._send_at_cmd(cmd)

    def read_rest(self):
        while self._ser.in_waiting:
            print(self._ser.readline())
            print(self._ser.readline())
            sleep(0.400)

    def clear_rx_buffer(self):
        _ = self._ser.read(self._ser.inWaiting())  # Clear buffer

    def set_to_text_mode(self):
        cmd = b"AT+CMGF=1\r"
        return self._send_at_cmd(cmd)

    def set_contact_number(self, contact_number):
        cmd = b"AT+CMGS=\"" + bytes(contact_number, "utf-8") + b"\"\r"
        return self._send_at_cmd(cmd)

    def is_ready(self) -> bool:
        cmd = b"ATZ\r"
        return self._assert_ok(self._send_at_cmd(cmd))

    def delete_all_txt(self):
        cmd = b'AT+CMGDA="DEL ALL"\r'
        return self._send_at_cmd(cmd)

    def read_message(self):
        cmd = b"AT+CMGR=1\r"
        return self._clean_reply(self._send_at_cmd(cmd))

