import argparse

import config
from parse import Parse

from Init import *
from Compile import *

parse:argparse.ArgumentParser

def main():
    global parse
    parse = argparse.ArgumentParser(description=config.data["helpers"]["description"])

    parse.add_argument("execute", choices=config.data["executes"].values(), help=config.data["helpers"]["execute"])
    parse.add_argument("token", nargs="?", default=config.data["tokens"]["default"], choices=config.data["tokens"].values(), help=config.data["helpers"]["tokens"])
    parse.add_argument("data", nargs="*", default="", help=config.data["helpers"]["data"])

    parse.add_argument(config.data["flags"]["autocompile"], config.data["flags-abbrv"]["autocompile"], action="store_true", help=config.data["flagsHelpers"]["flagcompile"])

    args = parse.parse_args()
    parseArgs(args)

def parseArgs(args):
    global parse
    p = Init(args, parse)
    Parse(p)

    p2 = Compile(args, parse)
    Parse(p2)

if __name__ == "__main__":
    main()
