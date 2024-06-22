import config
import data as code
from parse import InterfaceFlow

class Compile(InterfaceFlow):
    def start(self, args, metedata):
        if len(args.data) < 2:
            return [ code.FLOW_DATA_INVALID, "need path to IN and OUT" ]
        if args.autocompile == True:
            print("compile from dir project")
        else:
            print("compile")
        return [ code.FLOW_PASSED, "successfuly" ]
                        