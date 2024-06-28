import re

from interfaces.InterfaceFlow import InterfaceFlow
from modules.console import console

REGEX_VERSION_SEMANTIC = "v\d+.\d+.\d+"

class UpgradeProject(InterfaceFlow):
    def execute(self, metadata):
        if len(metadata.data) !=0 :
            version = metadata.data[0]
            isValide = re.findall(REGEX_VERSION_SEMANTIC, version)
            if len(isValide) == 1:
                console().print(f":white_check_mark: Upgrade to [green]{version}[/green] with succssefuly")
                return "err_ok"
            else: 
                console().print(f":warning: SemVer invalid [red]{version}[/red]")
                return "err_text_format"
        console().print(":thumbs_up: Upgrade to latest version with succssefuly")
        return "err_ok"
    
    def __str__(self):
        return "Upgrade CLI"