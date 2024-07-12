import json
import configparser

from flows import *
from modules.cache import Cache

CONFIGS_PATHS = {
    "cli_config": "configs/cli.ini",
    "cli_msg": "configs/mensages",
    "index_table": "configs/table.json" 
}

FLOWS = {
    "InitProject": InitProject.InitProject,
    "UpgradeProject": UpgradeProject.UpgradeProject,
    "Defeault": Defeault.Defeault
}

parse_config = configparser.ConfigParser()

cache = Cache()

def get_cli_data() -> dict:
    global cache
    
    if cache.get("cli_data") != None:
        return cache.get("cli_data")
    
    data = {}
    
    with open(CONFIGS_PATHS["cli_config"], "r") as config_file:
        parse_config.read_file(config_file)

    for section in parse_config.sections():
        data[section] = {}
        for option in parse_config.options(section):
            data[section][option] = parse_config.get(section, option)
    
    cache.set("cli_data", data)
    
    return data

def get_mensages():
    global cache

    if cache.get("mensages") != None:
        return cache.get("mensages")

    mensages_object = {}
    
    with open(CONFIGS_PATHS["cli_msg"], "r") as file:
        content = file.read()
        mensages = content.splitlines()
        
        for msg in mensages:
        
            if msg == "": continue
        
            data = msg.split("=")
            msgcode = data[1].split("->")
            mensages_object["err_" + data[0]] = { "msg": msgcode[0], "code": msgcode[1] }
        
    cache.set("mensages", mensages_object)
    
    return mensages_object

def get_flow_table() -> dict:
    with open(CONFIGS_PATHS["index_table"], "r") as file:
        content = file.read()
        table = json.loads(content)
        return table

def get_index(execute, token):
    if execute == get_cli_data()["executes"]["defeault"]:
        return "defeault"
    elif execute != get_cli_data()["executes"]["defeault"] and token == get_cli_data()["tokens"]["defeault"]:
        return execute
    return f"{execute} {token}"

def get_flag_data(value:str) -> dict:
    
    flag_data = value.split("?", 1)
    
    flag_names = flag_data[0].split("/")
    name_object = {}
    name_object["flagDefault"] = "--" + flag_names[0]
    name_object["flagAbbrv"] = "-" + flag_names[1]
    
    attributes_texts = flag_data[1].split("|")
    attributes_object = {}
    
    for attribute in attributes_texts:
        attr = attribute.split("=", 1)
        attributes_object[attr[0]] = attr[1]

        str_start = attributes_object[attr[0]][0]
        str_end = attributes_object[attr[0]][len(attributes_object[attr[0]])-1]
        str_hash = attributes_object[attr[0]][1:len(attributes_object[attr[0]])-1]

        if str_start == "!" and str_end == "!":
            attributes_object[attr[0]] = get_cli_data()["flagshelpers"].get(str_hash, "erro: missing hash")
        
        if attr[0] == "choices":
            attributes_object[attr[0]] = json.loads(attr[1])
        
        if attr[0] == "nargs":
            try:
                attributes_object[attr[0]] = int(attr[1])
            except Exception as e:
                pass
    
    return { "flag": name_object, "attributes": attributes_object }