import data

class InterfaceFlow:
    def start(self, args, metadata):
        raise NotImplementedError("function no body")

class Parse:
    def __init__(self, flow:InterfaceFlow, parse, args, metadata):
        exitData= flow.start(args, metadata)
        if exitData[0] != data.FLOW_PASSED:
            parse.error(exitData[1])
