from abc import ABC, abstractmethod

class ExecutersInterface(ABC):
    @abstractmethod
    def execute(self):
        pass