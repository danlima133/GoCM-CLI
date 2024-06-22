import argparse

import config
import data

from parse import Parse

parse:argparse.ArgumentParser

def main():
    global parse
    parse = argparse.ArgumentParser(description=config.data["helpers"]["description"])

    parse.add_argument("execute", choices=config.data["executes"].values(), help=config.data["helpers"]["execute"])
    parse.add_argument("token", nargs="?", default=config.data["tokens"]["default"], choices=config.data["tokens"].values(), help=config.data["helpers"]["tokens"])
    parse.add_argument("data", nargs="*", default="", help=config.data["helpers"]["data"])
    
    parse.add_argument(config.formatToFlag(config.data["flags"]["autocompile"], False), config.formatToFlag(config.data["flags-abbrv"]["autocompile"], True), action="store_true", help=config.data["flagsHelpers"]["flagcompile"])

    args = parse.parse_args()

    index = data.getIndex(args.execute, args.token)
    flowTable = data.getFlowTable()
    flowData = flowTable.get(index, data.FLOW_NOT_FOUND)
    
    if flowData == data.FLOW_NOT_FOUND:
        parse.error("combination args failed")
        quit()
    
    flow = data.FLOWS[flowData[0]]
    Parse(flow, parse, args, flowData[1])

if __name__ == "__main__":
    main()
