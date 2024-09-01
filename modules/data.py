import json
import configparser

from flows import *

CONFIGS_PATHS = {
    "cli_config": "configs/cli.ini",
    "cli_msg": "configs/mensages",
    "index_table": "configs/table.json" 
}

FLOWS = {
    "InitProject": InitProject.InitProject,
    "UpgradeProject": UpgradeProject.UpgradeProject,
    "Flags": Flags.Flags
}

parse_config = configparser.ConfigParser()
cli_data = {}

def get_cli_data() -> dict:
    data = {}
    with open(CONFIGS_PATHS["cli_config"], "r") as config_file:
        parse_config.read_file(config_file)

    for section in parse_config.sections():
        data[section] = {}
        for option in parse_config.options(section):
            data[section][option] = parse_config.get(section, option)
    return data

cli_data = get_cli_data()

def get_flow_table() -> dict:
    with open(CONFIGS_PATHS["index_table"], "r") as file:
        content = file.read()
        table = json.loads(content)
        return table

def get_index(execute, token):
    if execute == cli_data["executes"]["default"]:
        return "default"
    elif execute != cli_data["executes"]["default"] and token == cli_data["tokens"]["default"]:
        return execute
    return f"{execute} {token}"

def get_flag_data(value:str) -> dict:
    global cli_data
    
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
            attributes_object[attr[0]] = cli_data["flagshelpers"].get(str_hash, "erro: missing hash")
        
        if attr[0] == "choices":
            attributes_object[attr[0]] = json.loads(attr[1])
        
        if attr[0] == "nargs":
            try:
                attributes_object[attr[0]] = int(attr[1])
            except Exception as e:
                pass
    
    return { "flag": name_object, "attributes": attributes_object }