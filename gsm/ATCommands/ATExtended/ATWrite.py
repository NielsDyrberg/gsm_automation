import attrs, attr

@attr.s
class ATWrite:
    cmd = attr.ib()
    cmd_argument = attr.ib()


    def to_string(self) -> str:
        pass

    @classmethod
    def from_string(cls, encapsulated_cmd):
        # Extract
        if not encapsulated_cmd.__contains__("="):
            raise AttributeError("encapsulated_cmd does not contain '='")

        cmd, cmd_argument = encapsulated_cmd.split("=")
        return cls(cmd, cmd_argument)