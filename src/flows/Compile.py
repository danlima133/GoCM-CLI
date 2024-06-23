from parse import InterfaceFlow

class Compile(InterfaceFlow):
    def start(self, args, metedata):
        paths = args.data
        if len(args.data) < 2 and args.autocompile == False:
            output = input("insert paths: ")
            data = output.split(" ")
            if len(data) < 2:  
                return "err_data"
            paths = data
        if args.autocompile == True:
            print("compile from dir project")
        else:
            print("compile")
            print(f"paths: {paths}")
        return "err_ok"
                        