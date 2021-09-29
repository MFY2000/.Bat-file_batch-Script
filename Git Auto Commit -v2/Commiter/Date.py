import ctypes, sys, win32api
from datetime import datetime
import time


class _Date:
    #(2019,9,7,22,9,10,10,0)# Year, # Month, # Day, # Hour, # Minute, # Second, # Millisecond

    def setDate(self, time_tuple):
        win32api.SetSystemTime(time_tuple)

    def getDate(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def getFullDate(self):
        return datetime.now()

    def getDaysDiffer(self, startDate, endDate):
        dateDiffer = startDate - endDate
        return dateDiffer.days

    def makeDate(self,month,day,year):

        tt = datetime.utcnow().time()
        win32api.SetSystemTime(year, month, 0, day,tt.hour, tt.minute, tt.second, (tt.microsecond//1000))

        # CommitTime = (year, month, 0, day,tt.hour, tt.minute, tt.second, (tt.microsecond//1000))
        # _Date.setDate(self,CommitTime)
        # return (CommitTime)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False



def main():
    if is_admin():
        _Date().makeDate(2,15,2004)
    else:
         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

         
    # CurrentDate = datetime.now().strftime("%Y,%m,%d,%H,%M,%S")
    
    # ShitDate = datetime.now().strftime("2020,9,1,21,9,10,10,0")
    # print(CurrentDate)


if __name__ == '__main__':
    main()