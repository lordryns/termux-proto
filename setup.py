import subprocess
import os
import time
import questionary
from rich.console import Console
from dataclasses import dataclass

@dataclass(slots=True)
class Setup:
    username: str
    c_compiler: str
    text_editor: str
    languages: list[str]

setup = Setup("", "")

def clear():
    subprocess.run("clear")


console = Console()

clear()
console.print("[bold green]Welcome to the termux-proto installer [/bold green]")
time.sleep(1)

def get_user_name() -> str:
    while True:
        name = questionary.text("set username:").ask()
        if len(name) > 1:
            return name
        console.print("[red]username cannot be left empty![/red]")



def get_c_compiler() -> str:
    choice = questionary.select("Select preferred C compiler",
                       ["clang", "gcc"])

    return choice.ask()


def get_text_editor() -> str:
    choice = questionary.select("Select preferred text editor",
                       ["vim", "kakoune", "helix", "neovim"])

    return choice.ask()


def main():
    setup.username = get_user_name()

    time.sleep(1)
    clear()

    setup.c_compiler = get_c_compiler()
    setup.text_editor = get_text_editor()

    print(f"name: {setup.username}\npreferred compiler: {setup.c_compiler}")



if __name__ == '__main__':
    main()

