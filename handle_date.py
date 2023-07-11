
from console import console
from datetime import datetime, timedelta


class Date():
    def get_date():
        return datetime.today().strftime("%Y-%m-%d")

    def today():
        with open("./current_date/current_date.txt", "w") as f:
            today = datetime.today().strftime("%Y-%m-%d")
            f.write(today)

    def yesterday():
        with open("./current_date/current_date.txt", 'r') as f:
            line = "".join(f.readline().split("/"))
            date = datetime.strptime(line, "%Y-%m-%d").date()
            newDate = date - timedelta(days=1)
            newDate = newDate.strftime("%Y-%m-%d")
            with open("./current_date/current_date.txt", 'w') as f:
                f.write(newDate)

    def advance_date(delta_time):
        with open("./current_date/current_date.txt", 'r') as f:
            line = "".join(f.readline().split("/"))
            date = datetime.strptime(line, "%Y-%m-%d").date()
            newDate = date + timedelta(days=delta_time)
            newDate = newDate.strftime("%Y-%m-%d")
            with open("./current_date/current_date.txt", 'w') as f:
                f.write(newDate)
            console.print(f"[green]Current day set to: {newDate}")

    def set_date(parsed_data):
        newDate = (parsed_data.d).date()
        newDate = newDate.strftime("%Y-%m-%d")
        with open("./current_date/current_date.txt", "w") as f:
            f.write(newDate)
        console.print(f"[green]Current day set to: {newDate}")

    def input_date(parsed_data):
        newDate = datetime.strftime(parsed_data.date, "%Y-%m-%d")
        with open("./current_date/current_date.txt", "w") as f:
            f.write(newDate)

    def getDateFromFile(type):
        if type == "str":
            with open("./current_date/current_date.txt") as f:
                line = "".join(f.readline().split("/"))
                date = datetime.strptime(line, "%Y-%m-%d").date()
                newDate = datetime.strftime(date, "%Y-%m-%d")
            return newDate
        elif type == "date":
            with open("./current_date/current_date.txt") as f:
                line = "".join(f.readline().split("/"))
                newDate = datetime.strptime(line, "%Y-%m-%d").date()
            return newDate

    def convertToString(date_object):
        return date_object.strftime("%Y-%m-%d")

    def convertToDateTime(date_string):
        datetime_obj = datetime.strptime(date_string, "%Y-%m-%d")
        return datetime_obj.date()
