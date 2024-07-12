from abc import ABC, abstractmethod

class InterfaceReadBook():
    def __init__(self, book):
        self.book = book
    
    @abstractmethod
    def read(self, page:int = 0):
        raise NotImplemented