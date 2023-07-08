import os
from inputParser import create_parser
from init import init_data
from handle_buy import handleBuy
from handle_sell import handleSell
# from modify_day.advance_time import handleAdvance
from modify_day.setDate import Date
from handle_report import handleReport


base_path = os.getcwd()
csv_path = os.path.join(base_path, "csv")
current_day_path = os.path.join(base_path, "day")


init_data(base_path, csv_path, current_day_path)


def main():
    # Accept arguments from argparse
    parser = create_parser()
    parsed = parser.parse_args()
    # Buy command was given and now parsed
    if hasattr(parsed, "buy"):
        handleBuy(parsed)
    # Sell command was given and now parsed
    if hasattr(parsed, "sell"):
        handleSell(parsed, csv_path)
    # Advanced command was given and now parsed
    if hasattr(parsed, "advance"):
        Date.advance_date(parsed.d)
    # Report command was given and now parsed
    if hasattr(parsed, "report"):
        handleReport(parsed)


if __name__ == "__main__":
    main()
