
from datetime import datetime,timedelta
import re
from git.db import GitCmdObjectDB
from git.repo.base import Repo
from Components import Status
from Components import Date

import ctypes, sys



class Git:
# Constructor
  def __init__(self, address):
    self.address = address
    self.repo = Repo(address, odbt = GitCmdObjectDB)
    self.status = Status.Status(self.repo)
    self.Date = Date._Date()
    self.message = self.Date.toString()

# to commit single file at a time
  def gitCommit_Single(self):
    count = 1

    for f in self.status.changes:
      self.repo.git.add(f)
      self.repo.git.commit('-m', self.message)
      print(f"git commit count: {count} Done")
      count += 1

    return count

# to commit number of files at a time
  def gitCommit_Number(self,file):

    self.repo.git.add(file)
    self.repo.git.commit('-m', self.message)

    return 1

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
      print("Git push done all changes")
    except:
      print('Some error occured while pushing the code') 

# to puch all the change by date
  def gitUndo(self):
    
    for i in range(len(list(self.repo.iter_commits('main')))):
      lst = list(self.repo.iter_commits('main'))
      print(i)
      self.repo.git.revert(lst[i], no_edit = True)



  def gitChange_date(self,Start,End):
  # Initailize Varrabile 
    CurrentDate = self.Date.getFullDate().strftime("%Y-%m-%d")
    NoOfDays_Differ = self.Date.getDaysDiffer(End,Start)
    countCommit = 0
  # 

  #Used to define the number of commit per day 
    if self.status.changes == 0:
      return
    
    elif (len(self.status.changes) / NoOfDays_Differ) > 1:
      countCommit = (int) (len(self.status.changes) / NoOfDays_Differ)
    
    elif (len(self.status.changes) / NoOfDays_Differ) < 1:
      NoOfDays_Differ = len(self.status.changes)
      countCommit = 1
    
    else:
      NoOfDays_Differ = 0
      countCommit = 0
    
  
      # countCommit = 1
    # _myDate.
    for i in range(NoOfDays_Differ):
      self.Date.setDate(Start.day,Start.month,Start.year)
      
      for j in range(countCommit):
        self.gitCommit_Number(self.status.changes[0])
        self.message = "Auto commits Done: "+self.Date.getDate()
        del self.status.changes[0]
      
      self.gitPush()
      print(self.Date.getDate())
      Start = Start + timedelta(days=1)
  
    self.Date.setDate(End.day,End.month,End.year)
    
    

# to run all the function 
  def run(self,_gateWay):
    count = 0
    if(_gateWay): 
      count = Git.gitCommit_all(self)
    else:
      count = Git.gitCommit_Single(self)

    Git.gitPush(self)

    return count

def main():  
  if is_admin():
    obj = Git(r"C:\Users\MFY\Desktop\Semeste_4_Spring-2021_")
    
    Start = datetime(2021,9,4)
    End = datetime(2021,10,11)

    # Feb 25, 2021 
    obj.gitChange_date(Start,End)

  else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    



def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

  # obj.run(False)

  # obj.main(False)

def runner():
  # obj = Git(r"C:\Users\MFY\Desktop\I-LOVE-GIT-COMMITS_")
  obj = Git(r"C:\Users\MFY\Desktop\Semeste_4_Spring-2021_")
  # obj = Git(r"C:\Users\MFY\Desktop\.Bat-file_batch-Script")
  # obj = Git(r"")
  # obj = Git(r"")
  # obj = Git(r"")
  # obj.run(False)
  obj.gitUndo()


if __name__ == '__main__':
  # runner()
  main()



