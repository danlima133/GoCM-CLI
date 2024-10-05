class FlowData:
    def __init__(self, flags = {}, args = {}, data = []):
        self.flags:dict = flags
        self.args:dict = args
        self.data:list = data