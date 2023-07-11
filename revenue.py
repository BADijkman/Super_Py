from console import console
from rich.align import Align
from datetime import datetime
# from modify_day.getDateFromFile import getDateFromFile
# from handle_cvs import getAllItemsSoldByDate
# from modify_day.date import get_date
from handle_date import Date
from handle_cvs import Sold


def displayRevenue(parsed_data):
    day = Date.getDateFromFile("str")
    totalRevenue = Sold.getAllItemsByDate(day, parsed_data)
    revenueLine = f"  Total revenue : \u20ac {totalRevenue:.2f}"
    if parsed_data.startingdate is None:
        display_date = Date.getDateFromFile("str")
        console.print()
        console.rule(f"[yellow]Revenue: {display_date}", style="yellow")
        console.print()
    elif parsed_data.startingdate is not None:
        display_date_from = Date.getDateFromFile("str")
        display_date_to = Date.get_date()
        console.print()
        console.rule(
            f"[yellow]Revenue: from {display_date_from} to {display_date_to}", style="yellow")
        console.print()
    console.print(revenueLine)
    console.rule(style="yellow")
    console.print(Align.right(
        f"[black]Dykey/Winc Copyright ©{(datetime.today().strftime('%Y'))}"))
    console.print()
