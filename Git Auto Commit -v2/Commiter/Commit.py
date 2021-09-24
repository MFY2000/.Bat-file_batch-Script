import os
import time
from datetime import datetime

CurrentDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def GitCommandRunner():
    os.system('cmd /c "git add -A && git commit -m \"MFY auto commit on"' + CurrentDate + '\""')


def push():
    os.system('cmd /c "git push -u origin"')


def Address():
    url = r"C:\Users\MFY\Desktop\I-LOVE-GIT-COMMITS"
    os.system('cmd /c "cd "'+url+' && Mkdir YourName"')
    # os.system('cmd /c "Mkdir YourName"')


def main():
  Address()
  # GitCommandRunner()
  # push()

if __name__ == '__main__':
    main()



