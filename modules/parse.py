class InterfaceFlow:
    def start(self, args, metadata):
        raise NotImplementedError("function no body")

class Parse:
    def __init__(self, flow:InterfaceFlow, args, metadata):
        self.flow = flow
        self.args = args
        self.metadata = metadata
    
    def execute(self):
        return self.flow.start(self.args, self.metadata)
