import calendar
import datetime
def checkFriday(month,year):
    date=datetime.date(year,month,13)

    # print(date)

    print(calendar.day_name[date.weekday()])

    if(date.weekday() == 4):
        return True
    return False

print("check ",checkFriday(1,2023))
print("check ",checkFriday(2,1985))



    