import re
from interfaces.InterfaceFlow import InterfaceFlow

REGEX_VERSION_SEMANTIC = "v\d+.\d+.\d+"

class UpgradeProject(InterfaceFlow):
    def execute(self, metadata):
        if len(metadata.data) !=0 :
            version = metadata.data[0]
            isValide = re.findall(REGEX_VERSION_SEMANTIC, version)
            if len(isValide) == 1:
                return "err_ok"
            else: return "err_data_invalid"
        return "err_ok"