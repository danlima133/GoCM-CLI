import argparse

from modules import data, mensage_error as erro
from modules.parse import Parse

parse:argparse.ArgumentParser

def main():
    global parse
    parse = argparse.ArgumentParser(description=data.cli_data["helpers"]["description"])

    parse.add_argument("execute", choices=data.cli_data["executes"].values(), help=data.cli_data["helpers"]["execute"])
    parse.add_argument("token", nargs="?", default=data.cli_data["tokens"]["default"], choices=data.cli_data["tokens"].values(), help=data.cli_data["helpers"]["tokens"])
    parse.add_argument("data", nargs="*", default="", help=data.cli_data["helpers"]["data"])

    for flag_value in data.cli_data["flags"].values():
        flag_data = data.get_flag_data(flag_value)
        parse.add_argument(flag_data["flag"]["flagDefault"], flag_data["flag"]["flagAbbrv"], **flag_data["attributes"])

    args = parse.parse_args()

    flow_table = data.get_flow_table()
    index = data.get_index(args.execute, args.token)
    flow_data = flow_table.get(index, erro.mensages["err_data"]["code"])
    
    if flow_data == erro.mensages["err_data"]["code"]:
        parse.error(erro.mensages["err_data"]["msg"])
    
    flow = data.FLOWS[flow_data[0]]
    process = Parse(flow, args, flow_data[1])
    err = process.execute()
    print(f"exit code: {erro.mensages[err]['code']} = {erro.mensages[err]['msg']}")

if __name__ == "__main__":
    main()
