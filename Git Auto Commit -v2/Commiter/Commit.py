
from datetime import datetime,timedelta
from git.db import GitCmdObjectDB
from git.repo.base import Repo
from Status import *
from Date import _Date
from Main import *



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
    print(Start)

    CurrentDate = self.Date.getDate()
    NoOfDays_Differ = self.Date.getDaysDiffer(End,Start)
    countCommit = 0


    if self.status.changes == 0:
      return
    elif NoOfDays_Differ >= len(self.status.changes):
      countCommit = 1
    elif NoOfDays_Differ >= (len(self.status.changes) / 2):
      countCommit = 2
    else:
      countCommit = len(self.status.changes) / NoOfDays_Differ
      # print("Error need to sort")

    # _myDate.
    for i in range(NoOfDays_Differ):
      self.Date.setDate(Start.day,Start.month,Start.year)
      Start = Start + timedelta(days=i)
      print(Start, "Start move to")
      for j in range(countCommit):
        self.message = "Auto commits Done: "+self.Date.getDate()
        print(self.Date.getDate(), "in working")
        # Git.gitCommit_Number(self,self.status.changes[j])
        del self.status.changes[j]

    self.Date.setDate(CurrentDate.day,CurrentDate.month,CurrentDate.year)
    # Git.gitPush(self)
    print(self.Date.getDate(), "After complete")

    input()

  def run(self,_gateWay):
    if(_gateWay): 
      Git.gitCommit_all(self)
    else:
      Git.gitCommit_Single(self)

    Git.gitPush()



def main():  
  if is_admin():
    
    obj = Git(r"C:\Users\MFY\Desktop\.Bat-file_batch-Script",("MFY auto commit at "+_Date().getDate()))
    
    Start = datetime(2021,9,28)
    End = datetime(2021,9,30)

    # Feb 25, 2021 
    obj.gitChange_date(Start,End)

  else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    



  # obj.run(False)

  # obj.main(False)


if __name__ == '__main__':
  main()
  