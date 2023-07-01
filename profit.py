# import csv
from console import console
# from rich.table import Table
from rich.align import Align
# from utils.utils import getItemFromBoughtCsvById
from datetime import datetime
from modify_day.getDateFromFile import getDateFromFile


def displayProfit():
    display_date = getDateFromFile("str")
    console.rule(f"[yellow]Profit: {display_date}", style="yellow")
    # console.print(Align.center(table))
    console.print(Align.right(
        f"[black]Dykey/Winc Copyright ©{(datetime.today().strftime('%Y'))}"))
