
# from git.db import GitCmdObjectDB
# from git.repo.base import Repo
from git import *
import os

def isFile(path):
    isExist = os.path.exists(path)
    if not isExist:
        return False

    try:
        Repo(path)
        return True
    except:
        return False

