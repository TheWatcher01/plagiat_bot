#!/usr/bin/python3
"""
    Plagiat Bot UserRepository components
    Utility to check for plagiarism at School
    Powered by JustGodWork & TheWatcher01
"""


from github import Repository, NamedUser


class UserRepository:
    """
        UserRepository class

        Attributes:
        user (NamedUser): GitHub user
        repository (Repository): user repository
    """

    def __init__(self, user: NamedUser, repository: Repository):
        assert user is not None, "Invalid user"
        assert repository is not None, "Invalid repository"
        self.user = user
        self.repository = repository
