from datetime import timedelta
from console import console, err_console
from modify_day.getDateFromFile import getDateFromFile


def handleAdvance(parsed_Data):
    advance_days = parsed_Data.d
    day = getDateFromFile("date")
    try:
        with open("./day/day.txt", "w") as f:
            newDay = day + timedelta(days=advance_days)
            euDay = newDay.strftime("%d/%m/%Y")
            console.print(f"[green]Current day set to: {euDay}")
            f.write(euDay)
        console.print("[green bold reverse]OK")
    except:
        err_console.print("Failure!")
