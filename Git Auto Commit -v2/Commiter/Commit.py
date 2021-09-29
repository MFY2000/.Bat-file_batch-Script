
from datetime import datetime
from git.db import GitCmdObjectDB
from git.repo.base import Repo
from Status import *
from Date import _Date
from Main import is_admin



class Git:
  # 
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
  def gitCommit_Number(self,file):

    self.repo.git.add(file)
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
  def gitChange_date(self,Start,End):
    NoOfDays_Differ = self.Date.getDaysDiffer(Start,End)
    countCommit = 0

    if self.status.changes == 0:
      return
    elif NoOfDays_Differ >= self.status.changes.len():
      countCommit = 1
    elif NoOfDays_Differ >= (self.status.changes.len() / 2):
      countCommit = 2
    else:
      print("Error need to sort")

    # _myDate.
    for i in range(NoOfDays_Differ):
      
      self.Date.setDate(Start.day+i,Start.month,Start.year)
      
      for j in range(countCommit):
        gitCommit_Number(self.status.changes[j])


  def run(self,_gateWay):
    if(_gateWay): 
      Git.gitCommit_all(self)
    else:
      Git.gitCommit_Single(self)

    Git.gitPush()



def main():  
  is_admin()
  obj = Git(r"C:\Users\MFY\Desktop\.Bat-file_batch-Script",("MFY auto commit at "+_Date().getDate()))

  obj.run(False)

  # obj.main(False)


if __name__ == '__main__':
  main()
  # print("hello")


    # if is_admin():
    #     _Date().makeDate(2,15,2004)
    # else:
    #      ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

  