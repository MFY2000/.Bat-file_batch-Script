from datetime import datetime
import os
from Components import Filling,Commit,Date

class AutoCommiter:
    def __init__(self):
        self.git = Filling.File2Data(r"C:\Users\DarkJoker\Desktop\Git-Auto-Commit\Address.txt").GitObj
        self.totalCommit = 0
        self.printing()
        self.userInput()


    def userInput(self):
        num = input("Enter number: ")
        
        while(not num.isdecimal):
            num = input("Enter number: ")

        index = (list(self.git))

        index = index[int(num)] 
        totalCommit = self.git[index]["CommiterRefernce"]
        if(len(totalCommit.status.changes) != 0):
            totalCommit = totalCommit.run(False)
            print(totalCommit)
        else:
            print("not Possible")


    def printing(self):
        print("=========================================================================")
        print("| S.NO | Name\t\t\t\t| Changes | Operation \t\t|")
        print("-------------------------------------------------------------------------")
        count = 1

        for i in self.git:
            temp = self.git[i]["CommiterRefernce"]
            print(f"|   {self.printProperly(count,3)}| {self.printProperly(i,30)} |    {self.printProperly(len(temp.status.changes),5)}| Single file Commit  |")
            count += 1
        print("-------------------------------------------------------------------------")

    def printProperly(self, name, lenght):
        name = str(name)

        toReturn = ""
        loopCounter = len(name)
        if(loopCounter > lenght):
            toReturn = name[0:lenght]
        else:
            
            toReturn = name + (" " * (lenght - loopCounter))

        return toReturn

    def fileWrite(self):
        self.FileData = open(r"C:\Users\DarkJoker\Desktop\Git-Auto-Commit\header.mfy","w+")
        self.FileData.write(self.totalCommit+"done on2"+datetime.now())


if __name__ == '__main__':
    
    i = 0
    while(True):
        command = 'cls'
        os.system(command)
        AutoCommiter()
    
    # cmd.run();