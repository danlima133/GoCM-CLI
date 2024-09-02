from interfaces import InterfaceFlow
from data.DataFlow import FlowData
from modules.console import console
from modules.cli import *

class Template(InterfaceFlow.InterfaceFlow):
    def execute(self, metadata:FlowData):
        if metadata.args.get("action", False):
            if metadata.args["action"] == "create":
                if len(metadata.data) > 0:
                    console().log(":sparkles: create new template")
                    console().log(f"Name: [green]{metadata.data[0]}")
                    return "err_ok"
                console().log("Template need name")
                return "err_data_invalid"
        return "err_command"
        #console().log(f"action: [red]{metadata.args["action"]}")
    
    def __str__(self):
        return "Template"