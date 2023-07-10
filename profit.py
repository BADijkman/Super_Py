from console import console
from rich.align import Align
from datetime import datetime
from handle_date import Date
from handle_cvs import Purchase, Sold


def displayProfit(parsed_data):
    day = Date.getDateFromFile("str")
    totalRevenue = Sold.getAllItemsByDate(day, parsed_data)
    totalPurchase = Purchase.getAllItemsByDate(day, parsed_data)
    totalProfit = totalRevenue - totalPurchase
    profitLine = f"  Total Profit : \u20ac {totalProfit:.2f}"
    if parsed_data.startingdate is None:
        display_date = Date.getDateFromFile("str")
        console.print()
        console.rule(f"[yellow]Profit: {display_date}", style="yellow")
        console.print()
    elif parsed_data.startingdate is not None:
        display_date_from = Date.getDateFromFile("str")
        display_date_to = Date.get_date()
        console.rule(
            f"[yellow]Profit: from {display_date_from} to {display_date_to}",
            style="yellow")
        console.print()
    console.print(profitLine)
    console.rule(style="yellow")
    console.print(Align.right(
        f"[black]Dykey/Winc Copyright ©{(datetime.today().strftime('%Y'))}"))
    console.print()
