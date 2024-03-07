#!/usr/bin/python3
"""
    Plagiat Bot RepoScanner components
    Utility to check for plagiarism at School
    Powered by JustGodWork & TheWatcher01
"""


from typing import Dict, List
from github import Repository
from asyncio import sleep
import components
import difflib


users = [
    "JustGodWork",
    "TheWatcher01",
]


class RepoScanner:
    """
        RepoScanner class
        This class is used to scan the repositories for plagiarism
    """

    def __init__(self):
        """
            Initialize the RepoScanner class
        """
        self.repos_by_name: Dict[str, List] = {}
        self.ratios: Dict[str, float] = {}

    def sort_repositories(self) -> Dict[str, List]:
        github = components.github
        user_repository = components.UserRepository
        for user in users:
            _user = github.get_user(user)
            if (_user is None):
                print(f"User {user} not found!")
                continue
            repos = _user.get_repos()
            for repo in repos:
                if (repo.name.find("holbertonschool-") == -1):
                    continue
                if (repo.name not in self.repos_by_name):
                    self.repos_by_name[repo.name] = []
                self.repos_by_name[repo.name].append(
                    user_repository(user=_user, repository=repo)
                )
        return self.repos_by_name

    def get_repository(self, repo_name: str) -> List:
        return self.repos_by_name.get(repo_name, [])

    def check_file(
            self,
            repository: Repository,
            target_repository: Repository,
            path: str = ""
    ):
        try:
            for file in repository.get_contents(path):
                if (file.type == "file"):
                    name = file.name
                    upper_name = name.upper()
                    if (name != ".gitignore" and upper_name != "README.MD"):
                        target_contents = target_repository.get_contents(path)
                        for target_file in target_contents:
                            t_name = target_file.name
                            t_path = target_file.path
                            if (name == t_name and file.path == t_path):
                                print(f"Starting scan of {path}/{file.name}")
                                diff = difflib.SequenceMatcher(
                                    None,
                                    file.content,
                                    target_file.content
                                )
                                plagiarism_ratio = components.PlagiarismRatio(
                                    user=repository.owner,
                                    repository=repository,
                                    target=target_repository.owner,
                                    target_repository=target_repository,
                                    filepath=f"{path}/{file.name}"
                                )
                                plagiarism_ratio.ratio = diff.ratio()
                elif (file.type == "dir"):
                    if (file.name != ".git"):
                        self.check_file(
                            repository,
                            target_repository,
                            file.path
                        )
        except Exception as err:
            print(f"Error: {err}")

    def check_by_repo(self, repo_name: str) -> List:
        user_repos = self.get_repository(repo_name)
        if (len(user_repos) < 2):
            return []
        for user_repo in user_repos:
            for target_repo in user_repos:
                if (user_repo == target_repo):
                    continue
                self.check_file(user_repo.repository, target_repo.repository)

    def start_scan(self):
        self.sort_repositories()
        # for repo in self.repos_by_name:
        #     print(f"Checking {repo}...")
        #     self.check_by_repo(repo)
        self.check_by_repo("holbertonschool-network")
        return self.ratios
