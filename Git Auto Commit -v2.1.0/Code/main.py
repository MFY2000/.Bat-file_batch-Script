from datetime import datetime

date_time_str = '1999/09/19 01:55:19'

date_time_obj = datetime.strptime(date_time_str, '%yy/%m/%y %H:%M:%S')


print ("The type of the date is now",  type(date_time_obj))
print ("The date is", date_time_obj)