from console import console
from rich.align import Align
from datetime import datetime
from handle_date import Date
from handle_cvs import Sold


def displayRevenue(parsed_data):
    if parsed_data.startingdate is None:
        day = Date.getDateFromFile("str")
        totalRevenue = Sold.getAllItemsByDate(day, parsed_data)
        revenueLine = f"  Total revenue : \u20ac {totalRevenue:.2f}"
        totalRevenue = Sold.getAllItemsByDate(day, parsed_data)
        revenueLine = f"  Total revenue : \u20ac {totalRevenue:.2f}"
        display_date = day
        console.print()
        console.rule(f"[yellow]Revenue: {display_date}", style="yellow")
        console.print()
    elif parsed_data.startingdate is not None:
        day = ((parsed_data.startingdate).date())
        day = Date.convertToString(day)
        totalRevenue = Sold.getAllItemsByDate(day, parsed_data)
        revenueLine = f"  Total revenue : \u20ac {totalRevenue:.2f}"
        display_date_from = day
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
