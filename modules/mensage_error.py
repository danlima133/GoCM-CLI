from modules.data import FILES_EXTERNS

mensages = {}

def get_msgs():
    mensages_object = {}
    with open(FILES_EXTERNS["cli_msg"], "r") as file:
        content = file.read()
        mensages = content.splitlines()
        for msg in mensages:
            data = msg.split("=")
            msgcode = data[1].split("::")
            mensages_object["err_" + data[0]] = { "msg": msgcode[0], "code": msgcode[1] }
        file.close()
    return mensages_object    

mensages = get_msgs()