from parse import InterfaceParse
import config

class Init(InterfaceParse):
    def __init__(self, args, parse):
        super().__init__(args, parse)
        
    def start(self):
        if self.args.execute == config.data["executes"]["init"]:
            print("initialize project")