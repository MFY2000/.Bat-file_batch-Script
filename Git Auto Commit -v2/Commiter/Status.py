import os
from git import Git , Repo, GitDB
from git.db import GitCmdObjectDB
from os import path


def main():
  Status()

untrack = []
modified = []

def Status():
  repo = Repo(Address(), odbt=GitCmdObjectDB)

  diff = repo.git.diff('HEAD~1..HEAD', name_only=True)

  for i in repo.untracked_files:
    untrack.append(i)

  changed = [ item.a_path for item in repo.index.diff(None) ]

  for item in repo.index.diff(None):
    print(item.a_path)

  for i in changed:
      modified.append(i)
      
  print(untrack, modified)






def Address():
  url = r"C:\Users\MFY\Desktop\.Bat-file_batch-Script"
  return url
    # os.system('cmd /c "cd C:\Users\MFY\Desktop\I-LOVE-GIT-COMMITS"')


if __name__ == '__main__':
    main()
