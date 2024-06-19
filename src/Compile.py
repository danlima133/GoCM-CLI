import config
from parse import InterfaceParse

class Compile(InterfaceParse):
    def __init__(self, args, parse):
        super().__init__(args, parse)
    
    def start(self):
        if self.args.execute == config.data["executes"]["compile"]:
            if self.args.token == config.data["tokens"]["member"]:
                if self.args.autocompile == True:
                    print("compile member (auto)")
                else:
                    if len(self.args.data) == 2:
                        print("compile member in " + self.args.data[0] + " to " + self.args.data[1])
                    else:
                        self.parse.error("paths not founds or not passeds")  
                        