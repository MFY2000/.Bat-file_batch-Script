import win32api
from datetime import datetime,date


class _Date:
    #(2019,9,7,22,9,10,10,0)# Year, # Month, # Day, # Hour, # Minute, # Second, # Millisecond

    def setDate(self, day, month, year):
        tt = datetime.utcnow().time()
        weekday = date(year, month, day).weekday()

        win32api.SetSystemTime(year, month, weekday, day,tt.hour, tt.minute, tt.second, (tt.microsecond//1000))

    def weekDay(self, year, month, day):
        offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        afterFeb = 1
        if month > 2: afterFeb = 0 
        aux = year - 1700 - afterFeb
        dayOfWeek  = 5
        dayOfWeek += (aux + afterFeb) * 365
        dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400
        dayOfWeek += offset[month - 1] + (day - 1)
        dayOfWeek %= 7

        return dayOfWeek


    def getDate(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def getFullDate(self):
        return datetime.now()

    def getDaysDiffer(self, startDate, endDate):
        dateDiffer = startDate - endDate
        return dateDiffer.days

    def toString(self):    
        return "MFY auto commit at "+self.getDate()

# def main():
    # CurrentDate = datetime.now().strftime("%Y,%m,%d,%H,%M,%S")
    
    # ShitDate = datetime.now().strftime("2020,9,1,21,9,10,10,0")
    # print(CurrentDate)

# if __name__ == '__main__':
#     main()