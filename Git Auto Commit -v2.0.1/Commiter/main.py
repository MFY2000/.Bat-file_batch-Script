from Components import Filling,Commit,Date

class AutoCommiter:
    def __init__(self):
        self.git = Filling.File2Data(r"C:\temp\Git Auto commit\Address.txt").GitObj
        self.printing()
        num = input("Enter number: ")
        self.git[num]["CommiterRefernce"].run(False)



    def printing(self):
        print("=========================================================================")
        print("| S.NO | Name\t\t\t\t| Changes |")
        print("-------------------------------------------------------------------------")
        count = 1

        for i in self.git:
            temp = self.git[i]["CommiterRefernce"]
            print(f"|   {self.printProperly(count,3)}| {self.printProperly(i,30)} |    {self.printProperly(len(temp.status.changes),5)}|")
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



if __name__ == '__main__':
    cmd = AutoCommiter()
    
    # cmd.run();