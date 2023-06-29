# import csv
from console import console, err_console
# from rich.table import Table
from rich.align import Align
# from utils.utils import getItemFromBoughtCsvById
from datetime import datetime
from datetime import timedelta
from utils.getDateFromFile import getDateFromFile
from utils.reset_day_to_today import reset_date_to_today


def handleRevenue(parsed_Data):
    # today
    if parsed_Data.today:
        reset_date_to_today()
        date = getDateFromFile("str")
        displayRevenue(date)
    # yesterday
    elif parsed_Data.yesterday:
        reset_date_to_today()
        # set date to yesterday
        date = getDateFromFile("date")
        with open("./day/day.txt", "w") as f:
            newDay = date + timedelta(days=-1)
            euDay = newDay.strftime("%d/%m/%Y")
            f.write(euDay)
        date_yesterday = getDateFromFile("str")
        displayRevenue(date_yesterday)
        # now
    elif parsed_Data.now:
        date = getDateFromFile("str")
        displayRevenue(date)
    # input date
    elif parsed_Data.date:
        date = datetime.strftime(parsed_Data.date, "%d/%m/%Y")
        with open("./day/day.txt", "w") as f:
            euDay = date
            f.write(euDay)
        displayRevenue(date)
    else:
        err_console.print(
            'error :inventory needs argument -- now --today --yesterday  or date')


def displayRevenue(date):
    console.rule(f"[yellow]Revenue: {date}", style="yellow")
    # console.print(Align.center(table))
    console.print(Align.right(
        f"[black]Dykey/Winc Copyright ©{(datetime.today().strftime('%Y'))}"))
