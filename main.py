import argparse

import data.DataFlow as structure
from modules import data, mensage_error as erro

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
    
    metadata = {}
    kwargs = args._get_kwargs()
    kwargs.remove(('execute', args.execute))
    kwargs.remove(('token', args.token))
    kwargs.remove(('data', args.data))

    flow_table = data.get_flow_table()
    index = data.get_index(args.execute, args.token)
    flow_data = flow_table.get(index, erro.mensages["err_command"]["code"])
    flow_args = {}
    try:
        flow_args = flow_data[1]
    except Exception:
        flow_args = {}

    if flow_data == erro.mensages["err_command"]["code"]:
        parse.error(erro.mensages["err_command"]["msg"])
    
    flow_metadata = structure.FlowData(flags=metadata, args=flow_args, data=args.data)
    flow = data.FLOWS[flow_data[0]]()
    err = flow.execute(flow_metadata)
    print(f"exit code: {erro.mensages[err]['code']} = {erro.mensages[err]['msg']}")

if __name__ == "__main__":
    main()
