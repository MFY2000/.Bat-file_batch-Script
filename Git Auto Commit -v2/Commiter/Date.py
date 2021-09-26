import sys
from _datetime import datetime

time_tuple = (2012,  # Year
              9,  # Month
              6,  # Day
              0,  # Hour
              38,  # Minute
              0,  # Second
              0,  # Millisecond
              )


def _win_set_time(time_tuple):
    import win32api
    dayOfWeek = datetime(*time_tuple).isocalendar()[2]
    t = time_tuple[:2] + (dayOfWeek,) + time_tuple[2:]
    win32api.SetSystemTime(*t)


import win32api
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def setDate():
    if is_admin():
        win32api.SetSystemTime(2020,9,1,21,9,10,10,0)
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


def main():
    CurrentDate = datetime.now().strftime("%Y,%m,%d,%H:%M:%S")
    ShitDate = datetime.now().strftime("2020,9,1,21,9,10,10,0")
    setDate()
    # input()
    # setDate(CurrentDate)
    print(CurrentDate)



if __name__ == '__main__':
    main()

