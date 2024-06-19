import os
import argparse

import config

def main():
    parse = argparse.ArgumentParser(description=config.data["helpers"]["description"])

    parse.add_argument("execute", choices=config.data["executes"].values(), help=config.data["helpers"]["execute"])
    parse.add_argument("token", nargs="?", default="null", choices=config.data["tokens"].values(), help=config.data["helpers"]["tokens"])
    parse.add_argument("data", nargs="*", default="", help=config.data["helpers"]["data"])

    args = parse.parse_args()
    parseArgs(args)

def parseArgs(args):
    print(args)

if __name__ == "__main__":
    main()

os.abort()
