import data.DataFlow as structure

from argparse import ArgumentParser, Namespace
from modules import data, mensage_error as erro
from modules.console import console

parse:ArgumentParser
args:Namespace

def get_metedata() -> dict:
    metadata = {}
    kwargs = args._get_kwargs()
    flags = kwargs[3::]
    for flag in flags:
        metadata[flag[0]] = flag[1]
    return metadata

def get_flow_data_by_table() -> list | dict:
    flow_table = data.get_flow_table()
    index = data.get_index(args.execute, args.token)
    flow_data = flow_table.get(index, erro.mensages["err_command"]["code"])
    flow_args = {}
    try:
        flow_args = flow_data[1]
    except Exception:
        flow_args = {}
    return flow_data, flow_args

def main():
    global parse
    global args
    
    parse = ArgumentParser(description=data.cli_data["helpers"]["description"], add_help=False)

    parse.add_argument("execute", nargs="?", default="null", choices=data.cli_data["executes"].values(), help=data.cli_data["helpers"]["execute"])
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
    console().rule("Execution Flow")
    console().log(f":arrows_clockwise: {flow}")
    err = flow.execute(flow_metadata)
    err_data = erro.mensages[err]
    err_code = err_data["code"]
    err_msg = err_data["msg"]
    console().rule("CLI Exit")
    console().log(f":book: exit: [red]code[/red]/{err_code} [red]mensage[/red]/{err_msg}")

if __name__ == "__main__":
    main()
