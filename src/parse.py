class InterfaceParse:
    def __init__(self, args, parse):
        self.args = args
        self.parse = parse
    
    def start(self):
        raise NotImplementedError("function no body")

class Parse:
    def __init__(self, parse:InterfaceParse):
        parse.start()