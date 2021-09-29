import ctypes, sys, win32api

def is_admin():
    try:
        ctypes.windll.shell32.IsUserAnAdmin()
    except:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

