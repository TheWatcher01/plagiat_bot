#!/usr/bin/python3
"""
    Plagiat Bot PlagiarismRatio components
    Utility to check for plagiarism at School
    Powered by JustGodWork & TheWatcher01
"""


from github import NamedUser, Repository


cache = []


class PlagiarismRatio:
    """
        PlagiarsimRatio class
        This class is used to store the
        plagiarism ratio between two repositories
    """

    def __init__(
            self,
            user: NamedUser,
            repository: Repository,
            target: NamedUser,
            target_repository: Repository,
            filepath: str
    ):
        self.user = user
        self.repository = repository
        self.target = target
        self.target_repository = target_repository
        self.ratio = 0
        self.filepath = filepath
        cache.append(self)

    @staticmethod
    def get_all():
        return cache

    @staticmethod
    def clear_cache():
        cache.clear()
        return cache
