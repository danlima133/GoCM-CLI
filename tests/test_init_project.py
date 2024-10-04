import unittest

from flows import InitProject
from data import DataFlow
from modules.console import console 

class TestInitProject(unittest.TestCase):
    def test_init_default(self):
        console().rule("Init Default")
        flow_data = DataFlow.FlowData(flags={"addon":False})
        flow = InitProject.InitProject()
        err = flow.execute(flow_data)
        self.assertEqual(err, "err_ok")
    
    def test_init_with_addon(self):
        console().rule("Init With Addon", )
        flow_data = DataFlow.FlowData(flags={"addon":True})
        flow = InitProject.InitProject()
        err = flow.execute(flow_data)
        self.assertEqual(err, "err_ok")
    
    def test_init_with_include(self):
        console().rule("Init With Include")
        flow_data = DataFlow.FlowData(flags={"include":["aaa", "bbb", "ddd"]})
        flow = InitProject.InitProject()
        err = flow.execute(flow_data)
        self.assertEqual(err, "err_ok")
    
    def test_init_no_include(self):
        console().rule("Init No Include")
        flow_data = DataFlow.FlowData(flags={"include":None})
        flow = InitProject.InitProject()
        err = flow.execute(flow_data)
        self.assertEqual(err, "err_ok")

if __name__ == "__main__":
    unittest.main()
