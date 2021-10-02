from Commit import *
from Date import _Date


class File2Data:
  def __init__(self, address):
    self.FileData = open(address,"r+")
    self.GitList = []

  def getData(self):
    
    for address in self.FileData.readlines():
      self.GitList.append(Git(address))
      
    
    self.FileData.close()



def main():
  obj = File2Data(r"C:\temp\Git Auto commit\Address.txt");
  obj.getData()
  




if __name__ == '__main__':
  main()
  