import os
from git import Git , Repo, GitDB
from git.db import GitCmdObjectDB
from os import path


def main():
  Status()

def Status():
  repo = Repo(Address(), odbt=GitCmdObjectDB)
  print(repo)

def Address():
  url = r"C:\Users\MFY\Desktop\I-LOVE-GIT-COMMITS"
  return url
    os.system('cmd /c "cd C:\Users\MFY\Desktop\I-LOVE-GIT-COMMITS"')
