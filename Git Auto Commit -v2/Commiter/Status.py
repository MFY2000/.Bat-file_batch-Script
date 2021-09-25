from git import Repo
from git.db import GitCmdObjectDB



def Status(repo):

  untrack = [ item for item in repo.untracked_files ]
  modified = [ item.a_path for item in repo.index.diff(None) ]
  
  changes = untrack + modified
  return changes


def isStatus(repo):
  result = repo.untracked_files != [] or repo.index.diff(None) != []
  return (result)




def main():
  print(isStatus(r"C:\Users\MFY\Desktop\.Bat-file_batch-Script"))



if __name__ == '__main__':
    main()
