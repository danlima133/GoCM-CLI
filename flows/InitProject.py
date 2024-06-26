from interfaces import InterfaceFlow as interface
from data import DataFlow as structure

class InitProject(interface.InterfaceFlow):
    def execute(self, metadata:structure.FlowData):
        includes = ["aaa", "bbb", "ccc"]

        flag_data = metadata.flags["addon"]
        flag_include = metadata.flags["include"]
        
        if flag_include != None:
            for file in flag_include:
                if file in includes:
                    print(f"include: {file}")
                else:
                    print(f"file can not include: {file}")

        if flag_data:
            print("project created with dir addon")
            return "err_ok"
        print("project created")
        return "err_ok"