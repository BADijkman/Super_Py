# import csv
from console import console, err_console
# from rich.table import Table
from rich.align import Align
# from utils.utils import getItemFromBoughtCsvById
from datetime import datetime
from modify_day.getDateFromFile import getDateFromFile
from utils.utils import getAllItemsSoldByDate
from date import get_date


def displayRevenue(parsed_data):

    day = getDateFromFile("str")
    totalRevenue = getAllItemsSoldByDate(day, parsed_data)
    revenueLine = f"  Total revenue : \u20ac {totalRevenue:.2f}"
    if parsed_data.startingdate is None:
        display_date = getDateFromFile("str")
        console.print()
        console.rule(f"[yellow]Revenue: {display_date}", style="yellow")
    elif parsed_data.startingdate is not None:
        display_date_from = getDateFromFile("str")

        display_date_to = get_date()
        console.rule(
            f"[yellow]Revenue: from {display_date_from} to {display_date_to}", style="yellow")
        console.print()
    console.print(revenueLine)
    console.rule(style="yellow")
    console.print(Align.right(
        f"[black]Dykey/Winc Copyright ©{(datetime.today().strftime('%Y'))}"))
