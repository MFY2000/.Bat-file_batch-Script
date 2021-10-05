
from datetime import datetime,timedelta
from git.db import GitCmdObjectDB
from git.repo.base import Repo
from Status import Status
from Date import _Date
from Main import is_admin
import ctypes, sys



class Git:
# Constructor
  def __init__(self, address):
    self.address = address
    self.repo = Repo(address, odbt = GitCmdObjectDB)
    self.status = Status(self.repo)
    self.Date = _Date()
    self.message = self.Date.toString()

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

# to puch all the change by date
  def gitChange_date(self,Start,End):
  # Initailize Varrabile 
    CurrentDate = self.Date.getDate()
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
      # print("Error need to sort")

  # 
      # countCommit = 1
    # _myDate.
    for i in range(NoOfDays_Differ):
      self.Date.setDate(Start.day,Start.month,Start.year)
      Start = Start + timedelta(days=i)
      for j in range(countCommit):
        # Git.gitCommit_Number(self,self.status.changes[0])
        self.message = "Auto commits Done: "+self.Date.getDate()
        print(self.Date.getDate(), "in working")
        del self.status.changes[0]
        # print(j,i, " adaad " , countCommit,NoOfDays_Differ)
        
    a = input()
      

      # print(Start, "Start move to", i)
      #   input()
    
    self.Date.setDate(CurrentDate.day,CurrentDate.month,CurrentDate.year)
    print(self.Date.getDate(), "After complete")
    input()
    # Git.gitPush(self)

# to run all the function 
  def run(self,_gateWay):
    if(_gateWay): 
      Git.gitCommit_all(self)
    else:
      Git.gitCommit_Single(self)

    Git.gitPush(self)



def main():  
  if is_admin():
    
    obj = Git(r"C:\Users\MFY\Desktop\.Bat-file_batch-Script",("MFY auto commit at "+_Date().getDate()))
    
    Start = datetime(2021,6,27)
    End = datetime(2021,9,4)

    # Feb 25, 2021 
    obj.gitChange_date(Start,End)

  else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    



  # obj.run(False)

  # obj.main(False)

def runner():
  # obj = Git(r"C:\Users\MFY\Desktop\I-LOVE-GIT-COMMITS_")
  obj = Git(r"C:\Users\MFY\Desktop\Jawan-Pakistan_Mobile-Hybrid-App-Dev-Using-Flutter_")
  # obj = Git(r"C:\Users\MFY\Desktop\.Bat-file_batch-Script")
  # obj = Git(r"")
  # obj = Git(r"")
  # obj = Git(r"")
  obj.run(False)


if __name__ == '__main__':
  runner()
  