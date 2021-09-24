import os
import time
from datetime import datetime
from Status import *
from git import Repo
from git.db import GitCmdObjectDB



CurrentDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def gitCommit(address, message):
  repo = Repo(address, odbt = GitCmdObjectDB)

  for f in Status(address):
    repo.git.add(f)
    repo.git.commit('-m', message)



def push():
    os.system('cmd /c "git push -u origin"')




def main():
  # print(Status(r"C:\Users\MFY\Desktop\.Bat-file_batch-Script"))
  gitCommit(r"C:\Users\MFY\Desktop\.Bat-file_batch-Script", "MFY auto commit at "+CurrentDate)




if __name__ == '__main__':
    main()


