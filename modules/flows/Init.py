from modules.parse import InterfaceFlow

class Init(InterfaceFlow):
    def __init__(self):
        super().__init__()
        
    def start(self, args, metadata):
        if args.addon == True:
            print("initialze project with dir addon")
            return "err_ok"
        print("initialize project")
        return "err_ok"