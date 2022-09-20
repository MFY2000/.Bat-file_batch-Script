from git.db import GitCmdObjectDB
from git.repo.base import Repo
from datetime import datetime, timedelta

import csv, os, ctypes, sys, win32api


class Committer:
    def __init__(self, address, startDate, difference):
        self.message = "updating 'readme' for more information on "

        self.address = address
        self.startDate = startDate
        self.currentDate = startDate
        self.difference = difference

        self.repo = Repo(address, odbt=GitCmdObjectDB)
        self.changes = []


    def status(self):
        untrack = [ item for item in self.repo.untracked_files ]
        modified = [ item.a_path for item in self.repo.index.diff(None) ]

        return untrack + modified


    def CommitCode(self):


        for f in range(self.difference):
            self.currentDate.setDate()

            file = open((self.address + "/.gitattributes"), "a+")
            file.write(f"git commit of day {f} on {self.currentDate.toString()} has been Done. \n")
            file.close()

            [self.repo.git.add(f) for f in self.status()]

            self.message += self.currentDate.toString()
            self.repo.git.commit('-m', self.message)

            self.currentDate.incraseDateCount()

            print("Commit Done")


class DateTime:
    def __init__(self, dateString):
        self.date = datetime.strptime(dateString, "%d/%m/%Y").date()

    def incraseDateCount(self):
        self.date = self.date + timedelta(days=1)

    def dateDifference(self, endingDate):
        return (endingDate - self.date).days

    def setDate(self):
        tt = datetime.utcnow().time()

        year = self.date.year
        month = self.date.month
        day = self.date.day
        weekday = self.date.weekday()
        win32api.SetSystemTime(year, month, weekday, day, tt.hour, tt.minute, tt.second, (tt.microsecond // 1000))
        print(f"Date is Change now {self.toString()}", end='')

    def weekDay(self, year, month, day):
        offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        afterFeb = 1
        if month > 2: afterFeb = 0
        aux = year - 1700 - afterFeb
        dayOfWeek = 5
        dayOfWeek += (aux + afterFeb) * 365
        dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400
        dayOfWeek += offset[month - 1] + (day - 1)
        dayOfWeek %= 7

        return dayOfWeek

    def toString(self):
        return self.date.strftime('%A, %d-%B-%Y')


def main():
    reposList = getData()
    while (True):
        printing(reposList)
        choiceRepo = int(input("Enter your repo number: "))
        if choiceRepo >= 0 and choiceRepo <= len(reposList["Name"]):
            address = reposList["Address"][choiceRepo]
            StartDate = DateTime(input("Starting Date (DD/MM/YY) must fellow: "))
            EndingDate = DateTime(input("Ending Date (DD/MM/YY) must fellow: "))

            difference = StartDate.dateDifference(EndingDate.date)

            commit = Committer(address, StartDate, difference)
            commit.CommitCode()

def printing(reposList):
    command = 'cls'
    os.system(command)

    print("================================================")
    print("| S.NO | Name\t\t\t\t")
    print("------------------------------------------------")

    count = 0

    for index in reposList["Name"]:
        print(f"| {count} | {index}|")
        count = count + 1
    print("------------------------------------------------")


def getData():
    with open(r"../log.csv", 'r') as file:
        csv_file = csv.DictReader(file, fieldnames=None, restkey=None, restval=None, dialect='excel')
        dictData = {"Name": [], "Address": []}

        for row in csv_file:
            dictData["Name"].append(dict(row)["Name"])
            dictData["Address"].append(dict(row)["Address"])

    return dictData


if __name__ == '__main__':

    try:
        match = ctypes.windll.shell32.IsUserAnAdmin()
        if match:
            main()
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    except NameError:
            print(NameError)

