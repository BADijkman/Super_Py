# import csv
from console import console, err_console
# from rich.table import Table
from rich.align import Align
# from utils.utils import getItemFromBoughtCsvById
from datetime import datetime

from modify_day.getDateFromFile import getDateFromFile
from utils.utils import getAllItemsSoldByDate
# omzet


def displayRevenue():
    day = getDateFromFile("str")
    check_date = getDateFromFile("date")

    soldItems = getAllItemsSoldByDate(day)
    print(soldItems)

    # totalRevenue = getRevenueFromSoldItemsList(soldItems)
    # revenueTable = returnTableOfItems(soldItems, "revenue")
    # date = day
    # revenueLine = f"Today's revenue so far: \u20ac {totalRevenue:.2f}"


# display_date = getDateFromFile("str")
# console.rule(f"[yellow]Revenue: {display_date}", style="yellow")
# # console.print(Align.center(table))
# console.print(Align.right(
#     f"[black]Dykey/Winc Copyright ©{(datetime.today().strftime('%Y'))}"))
