
from datetime import datetime
from git.db import GitCmdObjectDB
from git.repo.base import Repo
from Status import Status
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
    _myDate = self.Date.getFullDate()
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
    for days in range(NoOfDays_Differ):
      for i in range(countCommit):
        self.Date.setDate()
        gitCommit_Number(self.status.changes[i])


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
    if is_admin():
        _Date().makeDate(2,15,2004)
    else:
         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

    


