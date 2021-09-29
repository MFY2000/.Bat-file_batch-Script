
from datetime import datetime
from git.db import GitCmdObjectDB
from git.repo.base import Repo
from Status import Status
from Date import *



class gitMain:
  def __init__(self, address,message):
    self.address = address
    self.repo = Repo(address, odbt = GitCmdObjectDB)
    self.message = message


  def gitCommit_Single(self):

    for f in Status(self.repo):
      self.repo.git.add(f)
      self.repo.git.commit('-m', self.message)

  def gitCommit_Number(self,number):

    changesList = Status(self.repo)

    for i in range(number):
      self.repo.git.add(changesList[i])
      self.repo.git.commit('-m', self.message)


# to commit all the change in a single time
  def gitCommit_all(self):

    for f in Status(self.repo):
      self.repo.git.add(f)

    self.repo.git.commit('-m', self.message)

# to puch all the change to the main
  def gitPush(self):
    try:
      origin = self.repo.remote(name='origin')
      origin.push()
    except:
      print('Some error occured while pushing the code') 

  def gitChange_date(self):
    setDate()
    gitCommit_Number()


  def main(self,gateWay):
    if(gateWay): 
      gitMain.gitCommit_all(self)
    else:
      gitMain.gitCommit_Single(self)

    gitMain.gitPush(self)



def main():
  is_admin()
  obj = gitMain(r"C:\Users\MFY\Desktop\.Bat-file_batch-Script",("MFY auto commit at "+getDate()))
  obj.main(False)


if __name__ == '__main__':
    main()


