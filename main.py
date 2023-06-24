import os
from inputParser import create_parser
from buy import handleBuy
from sell import handleSell
from init import init_data
from inventory import displayCurrentInventory


base_path = os.getcwd()
csv_path = os.path.join(base_path, "csv")

init_data(base_path, csv_path)


def main():
    # Accept arguments from argparse
    parser = create_parser()
    parsed = parser.parse_args()
    # Buy command was given and now parsed
    if hasattr(parsed, "buy"):
        handleBuy(parsed)
    # Sell command was given and now parsed
    if hasattr(parsed, "sell"):
        handleSell(parsed)
    # Report command was given and now parsed
    if hasattr(parsed, "report"):
        if hasattr(parsed, "inventory"):
            displayCurrentInventory()


if __name__ == "__main__":
    main()
