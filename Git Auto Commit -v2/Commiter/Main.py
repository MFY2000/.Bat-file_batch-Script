import ctypes, sys, win32api

def is_admin():
  if ctypes.windll.shell32.IsUserAnAdmin():
    print("Connnected.")
    # _Date().makeDate(2,15,2004)
  else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    

    
