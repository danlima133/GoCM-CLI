from modules.data import CONFIGS_PATHS

mensages = {}

def get_msgs():
    mensages_object = {}
    with open(CONFIGS_PATHS["cli_msg"], "r") as file:
        content = file.read()
        mensages = content.splitlines()
        for msg in mensages:
            if msg == "": continue
            data = msg.split("=")
            msgcode = data[1].split("->")
            mensages_object["err_" + data[0]] = { "msg": msgcode[0], "code": msgcode[1] }
        file.close()
    return mensages_object    

mensages = get_msgs()