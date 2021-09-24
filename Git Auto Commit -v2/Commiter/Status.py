from git import Repo
from git.db import GitCmdObjectDB



def Status(address):
  repo = Repo(address, odbt = GitCmdObjectDB)

  untrack = [ item for item in repo.untracked_files ]
  modified = [ item.a_path for item in repo.index.diff(None) ]
  
  changes = untrack + modified
  return changes


def isStatus(address):
  repo = Repo(address, odbt = GitCmdObjectDB)
  result = repo.untracked_files != [] or repo.index.diff(None) != []
  return (result)




def main():
  print(isStatus(r"C:\Users\MFY\Desktop\.Bat-file_batch-Script"))



if __name__ == '__main__':
    main()
