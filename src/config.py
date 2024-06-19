import configparser

config = configparser.ConfigParser()
data = {}

with open("cli.ini", "r") as configFile:
    config.read_file(configFile)

for section in config.sections():
    data[section] = {}
    for option in config.options(section):
        data[section][option] = config.get(section, option)

def formatToFlag(string, abbrv):
    if abbrv:
        return "-" + string
    return "--" + string