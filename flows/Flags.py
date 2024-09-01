from interfaces import InterfaceFlow
from data.DataFlow import FlowData
from modules.console import console

class Flags(InterfaceFlow.InterfaceFlow):
    def execute(self, metadata:FlowData):
        if metadata.flags["version"] == True:
            console().print("State: [purple]developement[/purple]")
            console().print("[green]v0.0.0[/green]")
        elif metadata.flags["help"] == True:
            console().print("[red]HELP[/red]")
        return "err_ok"
    
    def __str__(self):
        return "Flags"