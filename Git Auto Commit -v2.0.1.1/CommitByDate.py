from git.db import GitCmdObjectDB
from git.repo.base import Repo
from datetime import datetime,timedelta

import ctypes, sys

class Committer:
    def __init__(self, address, difference, startDate):
        self.address = address
        self.repo = Repo(address, odbt = GitCmdObjectDB)
        self.difference = difference
        self.startDate = startDate
        self.currentDate = startDate
        self.message = "updating 'readme' for more information on "

    def CommitCode(self):
        file = open((self.address + "/.gitattributes"), "a+")

        for f in range(self.difference):
            self.repo.git.add(f)
            self.message += self.currentDate
            self.repo.git.commit('-m', self.message)
            file.write(f"git commit of day {f} on {self.currentDate} has been Done. \n")
            self.updateDate()

        file.close()
    def updateDate(self):

        self.currentDate += 1


def main():
    obj = Git(r"C:\Users\MFY\Desktop\Semeste_4_Spring-2021_")

    Start = datetime(2021, 9, 4)
    End = datetime(2021, 10, 11)

    obj.gitChange_date(Start, End)


def printing(self):
    print("=========================================================================")
    print("| S.NO | Name\t\t\t\t")
    print("-------------------------------------------------------------------------")
    count = 0

    for i in 
    print(f"| {count} |")
    print(f"| {count} |")

    print("-------------------------------------------------------------------------")



if __name__ == '__main__':
    if ctypes.windll.shell32.IsUserAnAdmin():
        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

