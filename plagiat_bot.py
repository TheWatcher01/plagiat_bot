#!/usr/bin/python3
"""
    Plagiat Bot entry point
    Utility to check for plagiarism at School
    Powered by JustGodWork & TheWatcher01
"""


import cmd
import json
import components
from typing import Dict, List


class PlagiatBot(cmd.Cmd):

    prompt = "\033[96mPlagiatBot>\033[0m "

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_help(self, arg):
        """Display help information"""
        if arg:
            # If the argument is a known command, display its help text
            try:
                func = getattr(self, 'do_' + arg)
            except AttributeError:
                print('Unknown command: %s' % arg)
            else:
                print(func.__doc__)
        else:
            # If no argument was given, display help text for all commands
            commands = [cmd[3:] for cmd in dir(self) if cmd.startswith('do_')]
            print("Available commands:")
            for command in commands:
                print(command)
            print("Use 'help <command>' to get more info about a command.")

    def do_check(self, arg):
        """Check for plagiarism"""
        print("Checking for plagiarism...")
        print("This can take a while, please wait...")
        scanner = components.RepoScanner()
        scanner.start_scan()
        try:
            with open("cache.json", "w") as file:
                obj_json: Dict[str, List] = {}
                for plagiarism in components.PlagiarismRatio.get_all():
                    username = plagiarism.user.login
                    if (username not in obj_json):
                        obj_json[username] = []
                    obj_json[username].append({
                        "username": username,
                        "targetname": plagiarism.target.login,
                        "repository_name": plagiarism.repository.name,
                        "filepath": plagiarism.filepath,
                        "ratio": plagiarism.ratio
                    })
                json.dump(obj=obj_json, fp=file)
        except Exception as err:
            print(f"Error: {err}")
        print("Done!")


if (__name__ == "__main__"):
    PlagiatBot().cmdloop()
