import os
import time
from datetime import datetime
from Status import *
from git import Repo
from git.db import GitCmdObjectDB



CurrentDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def gitCommit(address):
  if(isStatus(address) is not True):
    return 0

  repo = Repo(address, odbt = GitCmdObjectDB)

  files = repo.git.diff(None, name_only=True)
  for f in files.split('\n'):
      
      repo.git.add(f)

  repo.git.commit('-m', 'test commit')



    # os.system('cmd /c "git add -A && git commit -m \"MFY auto commit on"' + CurrentDate + '\""')


def push():
    os.system('cmd /c "git push -u origin"')


def Address():
    url = r"C:\Users\MFY\Desktop\I-LOVE-GIT-COMMITS"



def main():
  # print(Status(r"C:\Users\MFY\Desktop\.Bat-file_batch-Script"))
  print(gitCommit(r"C:\Users\MFY\Desktop\.Bat-file_batch-Script"))




if __name__ == '__main__':
    main()


