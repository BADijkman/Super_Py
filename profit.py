from console import console
from rich.align import Align
from datetime import datetime
from modify_day.getDateFromFile import getDateFromFile
from utils.utils import getAllItemsSoldByDate, getAllItemsPurchaseByDate
from date import get_date


def displayProfit(parsed_data):
    day = getDateFromFile("str")
    totalRevenue = getAllItemsSoldByDate(day, parsed_data)
    totalPurchase = getAllItemsPurchaseByDate(day, parsed_data)
    totalProfit = totalRevenue - totalPurchase
    profitLine = f"  Total Profit : \u20ac {totalProfit:.2f}"
    if parsed_data.startingdate is None:
        display_date = getDateFromFile("str")
        console.print()
        console.rule(f"[yellow]Revenue: {display_date}", style="yellow")
        console.print()
    elif parsed_data.startingdate is not None:
        display_date_from = getDateFromFile("str")
        display_date_to = get_date()
        console.rule(
            f"[yellow]Profit: from {display_date_from} to {display_date_to}", style="yellow")
        console.print()
    console.print(profitLine)
    console.rule(style="yellow")
    console.print(Align.right(
        f"[black]Dykey/Winc Copyright ©{(datetime.today().strftime('%Y'))}"))
    console.print()
