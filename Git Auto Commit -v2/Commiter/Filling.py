import os
from Commit import *
from Date import _Date


class File2Data:
  def __init__(self, address):
    self.FileData = open(address,"r+")
    self.GitList = []

  def getData(self):
    for address in self.FileData.readlines():    
      address = self.removebr(address)

      if address != "":
        self.GitList.append(Git(address))
    
    self.FileData.close()

  def removebr(self,str):
    return (str.replace("\n",""))
  
  def getNameFromString(self,str):
    mylist = str.split(chr(92))
    return({mylist[-1]:str})


def main():
  obj = File2Data(r"C:\temp\Git Auto commit\Address.txt");
  obj.getData()
  



if __name__ == '__main__':
  main()
  

# myList = [r"C:\Users\MFY\Desktop\Jawan-Pakistan_Mobile-Hybrid-App-Dev-Using-Flutter_",
# r"C:\Users\MFY\Desktop\I-LOVE-GIT-COMMITS_",r"C:\Users\MFY\Desktop\.Bat-file_batch-Script",
# r"C:\Users\MFY\Desktop\Semeste_5_FALL-2021_",
# r"C:\Users\MFY\Desktop\Semeste_4_Spring-2021_"]


# for address in myList:
#   self.FileData.write(address+"\n")
  # self.GitList.update(File2Data.getNameFromString(self,r""+address))