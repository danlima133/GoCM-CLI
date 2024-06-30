from argparse import ArgumentParser, Namespace

from modules.console import console

class CLIArgumentParser(ArgumentParser):
    def error(self, message: str):
        console().rule("Erro To Execute Flow")
        console().print(f":warning: {message}")