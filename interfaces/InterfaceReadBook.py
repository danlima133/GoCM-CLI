class InterfaceReadBook():
    def __init__(self, book):
        self.book = book
    
    def read(self, page:int = 0):
        raise NotImplemented