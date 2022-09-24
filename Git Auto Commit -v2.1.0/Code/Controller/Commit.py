from git.db import GitCmdObjectDB
from git.repo.base import Repo

class Committer:
    def __init__(self, address):
        self.address = address
        self.repo = Repo(address, odbt = GitCmdObjectDB)
        self.totalCommit = 0

    def NoOfChanges(self):
        untrack = [item for item in self.repo.untracked_files]
        modified = [item.a_path for item in self.repo.index.diff(None)]

        print(untrack)

        return untrack + modified