import os
from inputParser import create_parser
from init import init_data
from buy import handleBuy
from sell import handleSell
from utils.advance_time import handleAdvance
from inventory import handleInventory
from revenue import handleRevenue
from profit import handleProfit


base_path = os.getcwd()
csv_path = os.path.join(base_path, "csv")
day_path = os.path.join(base_path, "day")


init_data(base_path, csv_path, day_path)


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
        handleAdvance(parsed)
    # Report command was given and now parsed
    if hasattr(parsed, "report"):
        if hasattr(parsed, "inventory"):
            handleInventory(parsed)
        elif hasattr(parsed, "revenue"):
            handleRevenue(parsed)
        elif hasattr(parsed, "profit"):
            handleProfit(parsed)


if __name__ == "__main__":
    main()
