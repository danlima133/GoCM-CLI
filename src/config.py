import json
import configparser

config = configparser.ConfigParser()
data = {}

with open("cli.ini", "r") as configFile:
    config.read_file(configFile)

for section in config.sections():
    data[section] = {}
    for option in config.options(section):
        data[section][option] = config.get(section, option)

def getFlagData(value:str) -> dict:
    global data
    
    flagData = value.split("?", 1)
    
    flagNames = flagData[0].split("/")
    nameObject = {}
    nameObject["flagDefault"] = "--" + flagNames[0]
    nameObject["flagAbbrv"] = "-" + flagNames[1]
    
    attributesTexts = flagData[1].split("|")
    attributesObject = {}
    
    for attribute in attributesTexts:
        attr = attribute.split("=", 1)
        attributesObject[attr[0]] = attr[1]

        strStart = attributesObject[attr[0]][0]
        strEnd = attributesObject[attr[0]][len(attributesObject[attr[0]])-1]
        strHash = attributesObject[attr[0]][1:len(attributesObject[attr[0]])-1]

        if strStart == "!" and strEnd == "!":
            attributesObject[attr[0]] = data["flagshelpers"].get(strHash, "erro: missing hash")
        
        if attr[0] == "choices":
            attributesObject[attr[0]] = json.loads(attr[1])
        
        if attr[0] == "nargs":
            try:
                attributesObject[attr[0]] = int(attr[1])
            except Exception as e:
                print("erro convert")
    
    return { "flag": nameObject, "attributes": attributesObject }