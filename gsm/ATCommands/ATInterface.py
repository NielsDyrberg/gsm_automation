

from .ATBasic import ATBasic
from .ATSParameter import ATSParameter
from .ATExtended.ATExtended import ATExtended

class ATInterface(ATSyntaxInterface):
    basic = ATBasic()
    sPar = ATSParameter()
    extended = ATExtended()
    syntaxList = [extended, sPar, basic] # Basic has to be last, as it is the one with the fewest requirements

    def build_command(self, cmd_to_encapsulate):
        pass

    def extract_command(self, encapsulated_cmd):
        at_strings = super().extract_command(encapsulated_cmd)

        if len(at_strings) == 0:
            return []

        extracted_commands = []

        for at_string in at_strings:
            for syntax in self.syntaxList:
                return_object = syntax.extract_command(at_string)
                if return_object is not None:
                    extracted_commands.append(return_object)

        return extracted_commands

    def _extract_at_indices(string_containing_at):
        return [i for i in range(len(string_containing_at)) if string_containing_at.startswith("AT", i)]

    def build_command(self, cmd_to_encapsulate):
        pass

    def extract_command(self, encapsulated_cmd):
        at_strings = []

        at_indices = self._extract_at_indices(encapsulated_cmd)
        if at_indices[0] == -1:
            return at_strings

        len_at_indices = len(at_indices)

        for i in range(0, len_at_indices):
            if i != len_at_indices-1:
                at_strings.append(encapsulated_cmd[i:i+1])
            else:
                at_strings.append(encapsulated_cmd[i:])

        return at_strings
