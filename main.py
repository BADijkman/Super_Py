import os
from inputParser import create_parser
from buy import handleBuy
from sell import handleSell
from init import init_data


base_path = os.getcwd()
data_path = os.path.join(base_path, "cvs")

init_data(base_path, data_path)


def main():
    # Accept arguments from argparse
    parser = create_parser()
    parsed = parser.parse_args()
    # Buy command was given and now parsed
    if hasattr(parsed, "buy"):
        handleBuy(parsed)

    if hasattr(parsed, "sell"):
        handleSell(parsed)


if __name__ == "__main__":
    main()
