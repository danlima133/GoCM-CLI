from parse import InterfaceFlow
import data as code

class Init(InterfaceFlow):
    def __init__(self):
        super().__init__()
        
    def start(self, args, metadata):
        print("initialize project")
        print(args.test)
        return [code.FLOW_PASSED, "successfuly"]