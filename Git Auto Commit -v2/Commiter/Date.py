import win32api
from datetime import datetime


class _Date:
    #(2019,9,7,22,9,10,10,0)# Year, # Month, # Day, # Hour, # Minute, # Second, # Millisecond

    def setDate(self, day, month, year):
        tt = datetime.utcnow().time()
        win32api.SetSystemTime(year, month, 0, day,tt.hour, tt.minute, tt.second, (tt.microsecond//1000))

    def getDate(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def getFullDate(self):
        return datetime.now()

    def getDaysDiffer(self, startDate, endDate):
        dateDiffer = startDate - endDate
        return dateDiffer.days
        


# def main():
    # CurrentDate = datetime.now().strftime("%Y,%m,%d,%H,%M,%S")
    
    # ShitDate = datetime.now().strftime("2020,9,1,21,9,10,10,0")
    # print(CurrentDate)

# if __name__ == '__main__':
#     main()