from datetime import timedelta
# from date import get_date
from console import console, err_console

from utils.getDateFromFile import getDateFromFile


def handleAdvance(parsed_Data):
    # print(parsed_Data.d)
    advance_days = parsed_Data.d
    day = getDateFromFile("date")
    try:
        with open("./day/day.txt", "w") as f:
            newDay = day + timedelta(days=advance_days)
            euDay = newDay.strftime("%d/%m/%Y")
            console.print(f"[green]Current day set to: {euDay}")
            f.write(euDay)
        console.print("[green bold]OK")
    except:
        err_console.print("Failure!")
