from datetime import timedelta
from modify_day.getDateFromFile import getDateFromFile


def set_day_to_yesterday():
    date = getDateFromFile("date")
    with open("./day/day.txt", "w") as f:
        newDay = date + timedelta(days=-1)
        euDay = newDay.strftime("%d/%m/%Y")
        f.write(euDay)
