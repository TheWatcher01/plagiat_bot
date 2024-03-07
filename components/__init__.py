#!/usr/bin/python3
"""
    Plagiat Bot components
    Utility to check for plagiarism at School
    Powered by JustGodWork & TheWatcher01
"""


import dotenv
from github import Github
from .repo_scanner import RepoScanner
from .user_repository import UserRepository
from .plagiarism_ratio import PlagiarismRatio


# Load the environment variables from the .env file
# This file contains the GitHub token used to connect to the API
# The token is used to authenticate the bot to the GitHub API
env = dotenv.dotenv_values(".env")

try:
    """
        Connect the bot to the GitHub API
        This component will be used to check for plagiarism
        If the connection fails, the program will print an error and exit
    """
    github = Github(login_or_token=env.get("GITHUB_TOKEN"))
except Exception as e:
    print(f"Error: {e}")
    exit()
