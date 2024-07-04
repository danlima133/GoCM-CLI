from interfaces import InterfaceFlow as interface
from data import DataFlow as structure
from modules.console import console

class InitProject(interface.InterfaceFlow):
    def execute(self, metadata:structure.FlowData):
        includes = ["aaa", "bbb", "ccc"]

<<<<<<< HEAD
        flag_data = metadata.flags.get("addon", None)
        flag_include = metadata.flags.get("include", None)
=======
        print(metadata.flags)
        flag_data = metadata.flags["addon"]
        flag_include = metadata.flags["include"]
>>>>>>> f12f11c1a593a5d38f0584762ec5f5b8054a9785
        
        if flag_include != None:
            for file in flag_include:
                if file in includes:
                    console().print(f":heavy_plus_sign: -> :file_folder: [green]{file}[/green]")
                else:
                    console().print(f":heavy_minus_sign: -> :file_folder: [red]{file}[/red]")

        if flag_data:
            console().print(":file_folder: Project created")
            console().print(":heavy_plus_sign: -> :file_folder: [green]Addon[/green]")
            return "err_ok"
        console().print(":file_folder: Project created")
        console().print(":heavy_minus_sign: -> :file_folder: [red]Addon[/red]")
        return "err_ok"
    
    def __str__(self):
        return "Init Project"