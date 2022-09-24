from Components import Commit

class File2Data:
  def __init__(self, address):
    self.FileData = open(address,"r+")
    self.GitObj = {}

    # to get the data from file
    self.getData()

  def getData(self):
    for address in self.FileData.readlines():    
      address = self.removeSymbol(address)

      if address != "":
        self.GitObj.update(self.getNameFromString(address))

    
    self.FileData.close()

  def removeSymbol(self,str):
      self.Symbol_lst = {"\n":""} #"$":" ","#":" ","[":" ","]":" ","/":" ",".":" ","_\n":"","_":" "

      for replaceStr,newStr in self.Symbol_lst.items():
        str = str.replace(replaceStr,newStr)

      return str

  def getNameFromString(self,str):
    mylist = str.split(chr(92))
    return({mylist[-1]: {
      "Address":str,
      "CommiterRefernce": Commit.Git(str),
      "NextSchdelus": "",
      "Type": "Single",
      "Status":"Running"

    }})


def main_Runner():
  obj = File2Data(r"C:\temp\Git Auto commit\Address.txt");
  # obj.getData()
  return (obj.GitObj)



if __name__ == '__main__':
  main_Runner()
  
