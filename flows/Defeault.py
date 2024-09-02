import json

from rich.table import Table

from interfaces import InterfaceFlow
from data.DataFlow import FlowData
from modules.console import console
from modules.cli import *

class Defeault(InterfaceFlow.InterfaceFlow):
    def execute(self, metadata:FlowData):
        #print(metadata.flags["register"])
        if metadata.flags["version"] == True:
            console().print("State: [purple]developement[/purple]")
            console().print("[green]v0.0.0[/green]")
            return "err_ok"
        elif metadata.flags["help"] == True:
            console().print("[red]HELP[/red]")
            return "err_ok"
        elif metadata.flags["register"] != None:
            registersData = {}
            with open("register.json", "r") as file:
                registersData = json.loads(file.read())
            for register in metadata.flags["register"]:
                data = register.split(":", 1)
                
                if len(data) == 1:
                    console().log(f":warning: register [underline][red]{data[0]}[/red][/underline] not valid, need value as [red]{data[0]}:value")
                    continue
                
                if data[1] == "":
                    try:
                        registersData.pop(data[0])
                        console().log(f":heavy_minus_sign: register [underline][red]{data[0]}[/red][/underline] removed")
                    except KeyError as erro:
                        console().log(f":card_index: register [underline][red]{data[0]}[/red][/underline] not exists to remove")
                    continue

                registersData[data[0]] = data[1]
                console().log(f":heavy_plus_sign: add register [underline][green]{data[0]}[/green][/underline] with value = [green]{data[1]}")
            if len(metadata.flags["register"]) == 0:
                table = Table(title="Registers")
                table.add_column("Key", justify="center")
                table.add_column("Value", justify="center")
                for register in registersData:
                    table.add_row(register, registersData[register])
                console().print(table)
            with open("register.json", "w") as file:
                file.write(json.dumps(registersData))
            return "err_ok"
        return "err_defeault"
    
    def __str__(self):
        return "Defeault"