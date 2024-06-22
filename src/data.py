import json
from flows import Init, Compile

FLOW_PASSED = 0
FLOW_DATA_INVALID = 1
FLOW_NOT_FOUND = 2

FLOWS = {
    "flow1": Init.Init(),
    "flow2":  Compile.Compile()
}

def getFlowTable() -> dict:
    with open("table.json", "r") as file:
        content = file.read()
        table = json.loads(content)
        return table

def getIndex(execute, token):
    if token == "null":
        return execute
    return execute + " " + token
