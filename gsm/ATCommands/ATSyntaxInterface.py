
from abc import ABC, abstractmethod

class ATSyntaxInterface(ABC):
    @abstractmethod
    def build_command(self, cmd_to_encapsulate):
        pass

    @abstractmethod
    def extract_command(self, encapsulated_cmd):
        pass
