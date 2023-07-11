import os
from inputParser import create_parser
from init import init_data
from handle_buy import handleBuy
from handle_sell import handleSell
from handle_date import Date
from handle_report import handleReport


base_path = os.getcwd()
csv_path = os.path.join(base_path, "csv")
current_day_path = os.path.join(base_path, "current_date")

# init
init_data(base_path, csv_path, current_day_path)


def main():
    parser = create_parser()
    parsed = parser.parse_args()
    if hasattr(parsed, "buy"):
        handleBuy(parsed)
    elif hasattr(parsed, "sell"):
        handleSell(parsed, csv_path)
    elif hasattr(parsed, "advance"):
        Date.advance_date(parsed.d)
    elif hasattr(parsed, "set"):
        Date.set_date(parsed)
    elif hasattr(parsed, "report"):
        handleReport(parsed)


if __name__ == "__main__":
    main()
