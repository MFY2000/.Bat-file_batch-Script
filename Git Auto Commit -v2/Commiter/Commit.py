from datetime import datetime
from Status import *

CurrentDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def gitCommit_Single(repo, message):

  for f in Status(repo):
    repo.git.add(f)
    repo.git.commit('-m', message)


def gitCommit_all(repo, message):

  for f in Status(repo):
    repo.git.add(f)

  repo.git.commit('-m', message)


def gitPush(repo):
  try:
    origin = repo.remote(name='origin')
    origin.push()
  except:
    print('Some error occured while pushing the code') 

def gitMain(address):
  repo = Repo(address, odbt = GitCmdObjectDB)
  
  gitCommit_all(repo, "MFY auto commit at "+CurrentDate)
  gitPush(repo)



def main():
  gitMain(r"C:\Users\MFY\Desktop\.Bat-file_batch-Script")
  



if __name__ == '__main__':
    main()


