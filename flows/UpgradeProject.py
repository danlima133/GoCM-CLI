from interfaces.InterfaceFlow import InterfaceFlow

class UpgradeProject(InterfaceFlow):
    def execute(self, metadata):
        print("upgrade CLI")
        return "err_ok"