import unittest

import modules.mensage_error as erro

from flows import UpgradeProject
from data import DataFlow

class TestUpgradeProject(unittest.TestCase):
    def test_execute_upgrade(self):
        flow_data = DataFlow.FlowData()
        flow = UpgradeProject.UpgradeProject()
        msg_exit = flow.execute(flow_data)
        print(erro.mensages[msg_exit]["msg"])
        self.assertEqual(msg_exit, "err_ok")
    
    def test_execute_upgrade_version_explicit(self):
        flow_data = DataFlow.FlowData(data=["v1.0.0"])
        flow = UpgradeProject.UpgradeProject()
        msg_exit = flow.execute(flow_data)
        print(erro.mensages[msg_exit]["msg"] + " " + "with version")
        self.assertEqual(msg_exit, "err_ok")
    
    def test_execute_upgrade_version_mistake(self):
        flow_data = DataFlow.FlowData(data=["v1.0"])
        flow = UpgradeProject.UpgradeProject()
        msg_exit = flow.execute(flow_data)
        print(erro.mensages[msg_exit]["msg"])
        self.assertEqual(msg_exit, "err_data_invalid")

if __name__ == "__main__":
    unittest.main()