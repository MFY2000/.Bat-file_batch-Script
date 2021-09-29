
from datetime import datetime
from git.db import GitCmdObjectDB
from git.repo.base import Repo
from Status import Status
from Date import _Date
from Main import is_admin



class Git:
  def __init__(self, address,message):
    self.address = address
    self.repo = Repo(address, odbt = GitCmdObjectDB)
    self.message = message
    self.status = Status(self.repo)
    self.Date = _Date()

# to commit single file at a time
  def gitCommit_Single(self):

    for f in self.status.changes:
      self.repo.git.add(f)
      self.repo.git.commit('-m', self.message)

# to commit number of files at a time
  def gitCommit_Number(self,number):

    changesList = self.status.changes

    for i in range(number):
      self.repo.git.add(changesList[i])
      self.repo.git.commit('-m', self.message)

# to commit all file at a time
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

# 
  def gitChange_date(self):
    _myDate = self.Date.getFullDate()
    # _myDate.

    self.Date.setDate()
    gitCommit_Number()


  def main(self,_gateWay):
    if(_gateWay): 
      Git.gitCommit_all()
    else:
      Git.gitCommit_Single()

    Git.gitPush()



def main():
  is_admin()
  obj = Git(r"C:\Users\MFY\Desktop\.Bat-file_batch-Script",("MFY auto commit at "+_Date().getDate()))
  obj.main(False)

  # f_date = date(2014, 7, 2)
  # l_date = date(2014, 7, 11)


if __name__ == '__main__':
    main()


