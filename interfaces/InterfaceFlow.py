from abc import ABC, abstractmethod

class InterfaceFlow(ABC):
    @abstractmethod
    def execute(self, metadata):
        raise NotImplementedError("function no body")
