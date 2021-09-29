import ctypes, sys, win32api
from datetime import datetime

time_tuple = (2019,9,7,22,9,10,10,0)# Year, # Month, # Day, # Hour, # Minute, # Second, # Millisecond

def is_admin():
    try:
        ctypes.windll.shell32.IsUserAnAdmin()
    except:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        

def setDate():
    # is_admin()
    win32api.SetSystemTime(time_tuple)


def getDate():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    

def main():
    CurrentDate = datetime.now().strftime("%Y,%m,%d,%H,%M,%S")
    # ShitDate = datetime.now().strftime("2020,9,1,21,9,10,10,0")
    setDate()
    # input()
    # setDate(CurrentDate)
    print(CurrentDate)



if __name__ == '__main__':
    main()

