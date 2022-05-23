import attrs, attr

from ATBasic import ATBasic
from ATSParameter import ATSParameter
from ATExtended.ATExtended import ATExtended

@attr.s
class ATCommands:
    type_list = [ATSParameter, ATExtended, ATBasic]  # Basic has to be last, as it is the one with the fewest requirements

    def to_string(self):
        pass

    @classmethod
    def from_string(cls, encapsulated_cmd):
        if not encapsulated_cmd.startswith("AT"):
            raise AttributeError("The command does not start with 'AT'")

        for at_type in cls.type_list:
            obj = at_type.from_string(encapsulated_cmd[2:])
            if obj is not None:
                return obj

        raise SyntaxError("No cmd matched encapsulated_cmd")

if __name__ == "__main__":
    obj = ATCommands.from_string("AT+CMGR=1")
    print(obj)