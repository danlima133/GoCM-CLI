import unittest
from modules.console import console

from flows import Defeault
from data import DataFlow

class TestDefeault(unittest.TestCase):
    def test_input_invalid(self):
        console().rule("Test Defeault - No Flags")
        flow = Defeault.Defeault()
        flow_data = DataFlow.FlowData({
            "version": False,
            "help": False,
            "register": None
        })
        err = flow.execute(flow_data)
        self.assertEqual(err, "err_defeault")
        console().log("No Flags")
        console().print(flow_data.flags)
    
    def test_flag_help(self):
        console().rule("Test Defeault - Flag Help")
        flow = Defeault.Defeault()
        flow_data = DataFlow.FlowData({
            "version": False,
            "help": True
        })
        err = flow.execute(flow_data)
        self.assertEqual(err, "err_ok")
        if flow_data.flags["help"]:
            console().log("Flag = [red]help[/red]")
            console().log(flow_data.flags)
    
    def test_flag_version(self):
        console().rule("Test Defeault - Flag Version")
        flow = Defeault.Defeault()
        flow_data = DataFlow.FlowData({
            "version": True,
            "help": False
        })
        err = flow.execute(flow_data)
        self.assertEqual(err, "err_ok")
        if flow_data.flags["version"]:
            console().log("Flag = [red]version[/red]")
            console().log(flow_data.flags)
    
    def test_register(self):
        console().rule("Test Defeault - Flag Register")
        flow = Defeault.Defeault()
        flow_data = DataFlow.FlowData({
            "version": False,
            "help": False,
            "register": ["testReg:testValue"]
        })
        err = flow.execute(flow_data)
        if flow_data.flags["register"] != None:
            console().log("Flag = [red]register[/red]")
            console().log(flow_data.flags)
        self.assertEqual(err, "err_ok")

if __name__ == "__main__":
    unittest.main()