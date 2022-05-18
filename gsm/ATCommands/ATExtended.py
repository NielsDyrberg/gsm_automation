
from .ATSyntaxInterface import ATSyntaxInterface
from overloading import overload

class ATExtended(ATSyntaxInterface):
    def build_command(self, cmd_to_encapsulate):
        cmd_to_encapsulate = super().build_command(cmd_to_encapsulate)
        cmd_to_encapsulate = cmd_to_encapsulate + "+"

    def build_command(self, cmd_to_encapsulate, ):

    def extract_command(self, encapsulated_cmd) -> list:
        return super().extract_command(encapsulated_cmd)

class EExtended:
    read_sms_message = "CMGR=1"