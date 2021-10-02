from Commit import *
from Date import _Date


class File2Data:
  def __init__(self, address):
    self.FileData = open(address,"r+")
    self.GitList = []

  def getData(self):
    
    # for address in self.FileData.readlines():

      # obj = Git(address)
      # obj.run(False)
    
    self.FileData.close()



def main():
  # obj = File2Data(r"C:\temp\Git Auto commit\Address.txt");
  # obj.getData()
  
  obj = Git(r"C:\Users\MFY\Desktop\mfy2000")
  obj.run(False)

  for i in range(10):
    print(i)


if __name__ == '__main__':
  main()
  