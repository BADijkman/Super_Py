
from console import console
from datetime import datetime, timedelta


class Date():
    # def __init__(self, date,):
    #     self.date = date

    def get_date():
        return datetime.today().strftime('%d/%m/%Y')

    def today():
        with open("./current_date/current_date.txt", "w") as f:
            today = datetime.today().strftime('%d/%m/%Y')
            f.write(today)

    def yesterday():
        with open("./current_date/current_date.txt", 'r') as f:
            line = "".join(f.readline().split("/"))
            date = datetime.strptime(line, "%d%m%Y").date()
            newDate = date - timedelta(days=1)
            newDate = newDate.strftime("%d/%m/%Y")
            with open("./current_date/current_date.txt", 'w') as f:
                f.write(newDate)

    def advance_date(delta_time):
        with open("./current_date/current_date.txt", 'r') as f:
            line = "".join(f.readline().split("/"))
            date = datetime.strptime(line, "%d%m%Y").date()
            newDate = date + timedelta(days=delta_time)
            newDate = newDate.strftime("%d/%m/%Y")
            with open("./current_date/current_date.txt", 'w') as f:
                f.write(newDate)
            console.print(f"[green]Current day set to: {newDate}")

    def input_date(parsed_data):
        newdate = datetime.strftime(parsed_data.date, "%d/%m/%Y")
        with open("./current_date/current_date.txt", "w") as f:
            f.write(newdate)

    def starting_date(parsed_data):
        newdate = datetime.strftime(parsed_data.startingdate, "%d/%m/%Y")
        with open("./current_date/current_date.txt", "w") as f:
            f.write(newdate)

    def getDateFromFile(type):
        if type == "str":
            with open("./current_date/current_date.txt") as f:
                line = "".join(f.readline().split("/"))
                date = datetime.strptime(line, "%d%m%Y").date()
                newdate = datetime.strftime(date, "%d/%m/%Y")
            return newdate
        elif type == "date":
            with open("./current_date/current_date.txt") as f:
                line = "".join(f.readline().split("/"))
                newdate = datetime.strptime(line, "%d%m%Y").date()
            return newdate

    def convertToString(date_object):
        return date_object.strftime("%d/%m/%Y")

    def convertToDateTime(date_string):
        datetime_obj = datetime.strptime(date_string, "%d/%m/%Y")
        return datetime_obj.date()
