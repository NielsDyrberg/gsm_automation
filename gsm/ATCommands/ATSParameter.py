
from .ATSyntaxInterface import ATSyntaxInterface

class ATSParameter(ATSyntaxInterface):
    def build_command(self, cmd_to_encapsulate):
        return super().build_command(cmd_to_encapsulate)

    def extract_command(self, encapsulated_cmd) -> list:
        return super().extract_command(encapsulated_cmd)
