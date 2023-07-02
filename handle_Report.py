from console import err_console
from modify_day.set_day_to_today import set_day_to_today
from modify_day.set_day_to_yesterday import set_day_to_yesterday
from modify_day.set_day_to_inputday import set_day_to_inputday
from modify_day.set_day_to_startingday import set_day_to_startingday
from inventory import displayInventory
from revenue import displayRevenue
from profit import displayProfit


def handleReport(parsed_Data):
    if hasattr(parsed_Data, 'inventory'):
        if parsed_Data.inventory:
            if parsed_Data.today:
                set_day_to_today()
                displayInventory()
            elif parsed_Data.yesterday:
                set_day_to_today()
                set_day_to_yesterday()
                displayInventory()
            elif parsed_Data.now:
                displayInventory()
            elif parsed_Data.date:
                set_day_to_inputday(parsed_Data)
                displayInventory()
            else:
                err_console.print(
                    'error :inventory needs argument: --today --yesterday --now--date ')

    elif hasattr(parsed_Data, 'profit'):
        if parsed_Data.profit:
            if parsed_Data.today:
                set_day_to_today()
                displayProfit()
            elif parsed_Data.yesterday:
                set_day_to_today()
                set_day_to_yesterday()
                displayProfit()
            elif parsed_Data.now:
                displayProfit()
            elif parsed_Data.date:
                set_day_to_inputday(parsed_Data)
                displayProfit()
            else:
                err_console.print(
                    'error :provit needs argument: --today  --yesterday --now --date')

    elif hasattr(parsed_Data, 'revenue'):
        if parsed_Data.revenue:
            if parsed_Data.today:
                set_day_to_today()
                displayRevenue(parsed_Data)
            elif parsed_Data.yesterday:
                set_day_to_today()
                set_day_to_yesterday()
                displayRevenue(parsed_Data)
            elif parsed_Data.now:
                displayRevenue(parsed_Data)
            elif parsed_Data.date:
                set_day_to_inputday(parsed_Data)
                displayRevenue(parsed_Data)
            elif parsed_Data.startingdate:
                set_day_to_startingday(parsed_Data)
                displayRevenue(parsed_Data)
            else:
                err_console.print(
                    'error :revenue needs argument: --today --yesterday --now --date --startingdate')

    else:
        err_console.print(
            'error :report needs argument: inventory profit revenue')
