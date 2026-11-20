from getpass import getpass
import sys 
import datetime
from utilities.async_util import timer, run_async
from utilities.quiz_util import CLUE
import subprocess

def clear_term():
    match sys.platform:
        case "win32":
            cmd = subprocess.run(["cls"], shell=True)
        case _:
            cmd = subprocess.run(["clear"])

class CLI:
    def __init__(self):
        import asyncio
        run_async(self._main())

    def _manual(self):
        man = [
            "quiz - Start the Quiz CLI",
            "help - Show this manual",
            "exit - Exit the CLI"
        ]
        for line in man:
            print(line)

    async def _quiz(self):
        options = [
            "login",
            "C.L.U.E",
            "exit"
        ]
        clear_term()
        banner = "Custom Learning & User Evaluator"
        div = "=" * len(banner)
        print(f"{banner}\n{div}\n")
        input_prefix = ""
        while True:
            command = input(f"{input_prefix}>>> ")
            match command.strip():
                case "login":
                    CLUE()
                case "exit":
                    clear_term()
                    print("Exiting quiz...")
                    await timer(2)
                    clear_term()
                    break

    async def _main(self):
        clear_term()
        banner = "Welcome to the CLI. enter 'help' for help and exit to quit"
        print(banner)
        while True:
            command = input(">>> ")
            match command.strip():
                case "help":
                    self._manual()
                case "exit":
                    clear_term()
                    print("Exiting script...")
                    await timer(2)
                    clear_term()
                    sys.exit()
                case "quiz":
                    await self._quiz()
                case _:
                    print(f"Unknown command: {command}")
            