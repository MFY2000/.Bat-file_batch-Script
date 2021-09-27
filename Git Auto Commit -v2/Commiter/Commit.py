
from datetime import datetime
from git.db import GitCmdObjectDB
from git.repo.base import Repo
from Status import Status
from Date import getDate



class gitMain:
  def __init__(self, address,message):
    self.address = address
    self.repo = Repo(address, odbt = GitCmdObjectDB)
    self.message = message


  def gitCommit_Single(self):

    for f in Status(self.repo):
      self.repo.git.add(f)
      self.repo.git.commit('-m', self.message)


  def gitCommit_all(self):

    for f in Status(self.repo):
      self.repo.git.add(f)

    self.repo.git.commit('-m', self.message)


  def gitPush(self):
    try:
      origin = self.repo.remote(name='origin')
      origin.push()
    except:
      print('Some error occured while pushing the code') 

  def main(self,gateWay):
    if(gateWay): 
      gitMain.gitCommit_all(self)
    else:
      gitMain.gitCommit_Single(self)

    gitMain.gitPush(self)



def main():
  obj = gitMain(r"C:\Users\MFY\Desktop\.Bat-file_batch-Script",("MFY auto commit at "+getDate()))
  obj.main(False)


if __name__ == '__main__':
    main()


