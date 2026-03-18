import subprocess
import os
import time
import questionary
from rich.console import Console


def clear():
    subprocess.run("clear")

NAME = None
PASSWORD = None 

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



def get_password() -> str:
    password = ""
    tries = 1
    
    while True:
        password = questionary.password("set password:").ask()
        if len(password) > 4:
            break

        console.print("[red]Password is too short!")


    while True:
        confirm_password = questionary.password("confirm password:").ask()
        if confirm_password == password:
            break

        console.print(f"[red]Password does not match, tries: {tries}/3")    
        tries += 1

        if tries > 3:
            break

    if tries > 3:
        clear()
        return get_password()

    return password

def main():
    global NAME, PASSWORD

    NAME = get_user_name()
    PASSWORD = get_password()

    time.sleep(1)
    clear()


if __name__ == '__main__':
    main()

