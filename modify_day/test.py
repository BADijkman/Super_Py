# from date import get_date
from datetime import datetime, timedelta
from getDateFromFile import getDateFromFile


class Date():
    def __init__(self, date):
        self.date = date

    def today():
        with open("./day/current_date.txt", "w") as f:
            today = datetime.today().strftime('%d/%m/%Y')
            f.write(today)
            print("set to today")

    def yesterday():
        with open("./day/current_date.txt", 'r') as f:
            line = "".join(f.readline().split("/"))
            date = datetime.strptime(line, "%d%m%Y").date()
            newDate = date + timedelta(days=-1)
            newDate = newDate.strftime("%d/%m/%Y")
            with open("./day/current_date.txt", 'w') as date_file:
                date_file.write(newDate)
            print("set to yesterday")

    def advance_date(delta_time):
        pass


Date.today()
Date.yesterday()
