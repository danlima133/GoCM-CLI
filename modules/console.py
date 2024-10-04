from rich.console import Console

def console() -> Console:
    output = Console(log_path=True)
    return output