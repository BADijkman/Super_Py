from datetime import datetime


def set_day_to_inputday(parsed_Data):
    date = datetime.strftime(parsed_Data.date, "%d/%m/%Y")
    with open("./day/day.txt", "w") as f:
        euDay = date
        f.write(euDay)
