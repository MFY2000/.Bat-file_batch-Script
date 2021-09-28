import ctypes, sys

# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False
    


# def runAsAdmin():
#   if not is_admin():
#      ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
#      print(is_admin())
    

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
