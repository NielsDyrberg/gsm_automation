import attrs, attr

@attr.s
class ATSParameter:
    at = "ATS"
    cmd = attr.ib()
    cmd_argument = attr.ib(default=None)

    def to_string(self) -> str:
        pass

    @classmethod
    def from_string(cls, encapsulated_cmd):
        pass
