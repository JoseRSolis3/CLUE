from getpass import getpass
import sys 
import datetime
from utilities.async_util import timer, run_async
from utilities.quiz_util import CLUE
import subprocess

clear_term = subprocess.run(["clear"])

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
            "exit"
        ]
        banner = "Starting quiz application..."
        print(banner)
        input_prefix = ""
        while True:
            command = input(">>> ")
            match command.strip():
                case "login":
                    CLUE()
                case "exit":
                    clear_term = subprocess.run(["clear"])
                    print("Exiting quiz...")
                    await timer(2)
                    clear_term = subprocess.run(["clear"])
                    break


            

    async def _main(self):
        banner = "Welcome to the CLI. enter 'help' for help and exit to quit"
        print(banner)
        while True:
            command = input(">>> ")
            match command.strip():
                case "help":
                    self._manual()
                case "exit":
                    clear_term = subprocess.run(["clear"])
                    print("Exiting script...")
                    await timer(2)
                    clear_term = subprocess.run(["clear"])
                    sys.exit()
                case _:
                    print(f"Unknown command: {command}")
            