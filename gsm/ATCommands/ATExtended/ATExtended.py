import inspect

import attrs, attr

from .ATWrite import ATWrite

@attr.s
class ATExtended:
    at = "AT+"
    cmd = attr.ib()
    cmd_argument = attr.ib(default=None)

    def to_string(self) -> str:
        pass

    @classmethod
    def from_string(cls, encapsulated_cmd):
        # Extract
        if not encapsulated_cmd.startswith("+"):
            return None

        has_equal = encapsulated_cmd.__contains__("=")
        has_question = encapsulated_cmd.__contains__("?")
        cmd_type = None

        if has_equal:
            if has_question:
                # Test
                pass
            else:
                # Write
                cmd_type = ATWrite
        elif has_question:
            # Read
            pass
        else:
            # Execution
            pass

        return cmd_type.from_string(encapsulated_cmd[1:])

class EExtended:
    read_sms_message = "CMGR=1"

if __name__ == "__main__":
    pass