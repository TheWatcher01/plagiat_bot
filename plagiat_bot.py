#!/usr/bin/python3
"""
    Plagiat Bot entry point
    Utility to check for plagiarism at School
    Powered by JustGodWork & TheWatcher01
"""


import cmd
import asyncio
import components


class PlagiatBot(cmd.Cmd):

    prompt = "\033[96mPlagiatBot>\033[0m "

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_help(self, arg):
        """
            Display help information
            Usage: help <command?>
        """
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

    def do_check(self, arg: str):
        """
            Check for plagiarism in all repositories
            Usage: check
        """
        print("Checking for plagiarism...")
        print("This can take a while, please wait...")
        scanner = components.RepoScanner()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(scanner.start_scan())
        print("Done!")

    def do_check_from_last(self, arg: str):
        """
            Check for plagiarism in all repositories (reverse order)
            Usage: check_from_last
        """
        print("Checking for plagiarism...")
        print("This can take a while, please wait...")
        scanner = components.RepoScanner()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(scanner.start_scan_from_last())
        print("Done!")

    def check_repo(self, arg: str):
        """
            Check for plagiarism in a specific repository
            Usage: check_repo <repository_name>
        """
        if (arg):
            args = arg.split()
            try:
                print(f"Checking for plagiarism in {args[0]}...")
                print("This can take a while, please wait...")
                scanner = components.RepoScanner()
                loop = asyncio.get_event_loop()
                loop.run_until_complete(scanner.start_scan(args[0]))
                print("Done!")
            except IndexError as err:
                print(f"Error: {err}")
        else:
            print("Error: Missing repository name")


if (__name__ == "__main__"):
    try:
        PlagiatBot().cmdloop()
    except Exception as e:
        print(f"\033[91mError in cmdLoop: {e}\033[0m")
        exit()
