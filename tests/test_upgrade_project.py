import unittest

from flows import UpgradeProject
from data import DataFlow
from modules.console import console
from modules import data

class TestUpgradeProject(unittest.TestCase):
    def test_execute_upgrade(self):
        console().rule("Upgrade Latest Version")
        flow_data = DataFlow.FlowData()
        flow = UpgradeProject.UpgradeProject()
        msg_exit = flow.execute(flow_data)
        print(data.get_mensages()[msg_exit]["msg"])
        self.assertEqual(msg_exit, "err_ok")
    
    def test_execute_upgrade_version_especific(self):
        console().rule("Upgrade Especific Version")
        flow_data = DataFlow.FlowData(data=["v1.0.0"])
        flow = UpgradeProject.UpgradeProject()
        msg_exit = flow.execute(flow_data)
        print(data.get_mensages()[msg_exit]["msg"] + " " + "with version")
        self.assertEqual(msg_exit, "err_ok")
    
    def test_execute_upgrade_version_format(self):
        console().rule("Upgrade Version Erro")
        flow_data = DataFlow.FlowData(data=["v1.0"])
        flow = UpgradeProject.UpgradeProject()
        msg_exit = flow.execute(flow_data)
        print(data.get_mensages()[msg_exit]["msg"])
        self.assertEqual(msg_exit, "err_text_format")

if __name__ == "__main__":
    unittest.main()