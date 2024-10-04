import sys
import data.DataFlow as structure

from modules.cli import CLIArgumentParser, Namespace
from modules import data, mensage_error as erro
from modules.console import console

import modules.pagination as pg

parse:CLIArgumentParser
args:Namespace

def get_metedata() -> dict:
    metadata = {}
    kwargs = args._get_kwargs()
    flags = kwargs[3::]
    for flag in flags:
        metadata[flag[0]] = flag[1]
    return metadata

def get_flow_data_by_table():
    flow_table = data.get_flow_table()
    index = data.get_index(args.execute, args.token)
    flow_data = flow_table.get(index, erro.mensages["err_not_found"]["code"])
    flow_args = {}
    try:
        flow_args = flow_data[1]
    except Exception:
        flow_args = {}
    return flow_data, flow_args

def main():
    global parse
    global args
    
    parse = CLIArgumentParser(description=data.cli_data["helpers"]["description"], add_help=False)

    parse.add_argument("execute", nargs="?", default="null", choices=data.cli_data["executes"].values())
    parse.add_argument("token", nargs="?", default=data.cli_data["tokens"]["defeault"], choices=data.cli_data["tokens"].values())
    parse.add_argument("data", nargs="*", default="")

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

    metadata = {}
    kwargs = args._get_kwargs()
    kwargs.remove(('execute', args.execute))
    kwargs.remove(('token', args.token))
    kwargs.remove(('data', args.data))
    for kwarg in kwargs:
        metadata[kwarg[0]] = kwarg[1]

    flow_table = data.get_flow_table()
    index = data.get_index(args.execute, args.token)
    flow_data = flow_table.get(index, erro.mensages["err_command"]["code"])
    flow_args = {}
    try:
        flow_args = flow_data[1]
    except Exception:
        flow_args = {}
    
    try:
        if flow_data == erro.mensages["err_command"]["code"]:
            parse.error(erro.mensages["err_command"]["msg"])
    except Exception:
        return erro.mensages["err_command"]["msg"]
    
    flow_metadata = structure.FlowData(flags=metadata, args=flow_args, data=args.data)
    flow = data.FLOWS[flow_data[0]]()
    console().rule("Execution Flow")
    console().log(f":arrows_clockwise: {flow}")
    err = flow.execute(flow_metadata)
    return err

if __name__ == "__main__":
    err = main()
    exit_code = erro.mensages[err]["code"]
    exit_msg = erro.mensages[err]["msg"]
    console().rule(f"CLI Exit: {exit_code}")
    console().log(f":book: {exit_msg}")
    sys.exit(exit_code)

