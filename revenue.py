# import csv
from console import console, err_console
# from rich.table import Table
from rich.align import Align
# from utils.utils import getItemFromBoughtCsvById
from datetime import datetime


def displayRevenue(date):
    console.rule(f"[yellow]Revenue: {date}", style="yellow")
    # console.print(Align.center(table))
    console.print(Align.right(
        f"[black]Dykey/Winc Copyright ©{(datetime.today().strftime('%Y'))}"))
