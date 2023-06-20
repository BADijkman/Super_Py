from inputParser import create_parser
from buy import handleBuy


def main():
    # Accept arguments from argparse
    parser = create_parser()
    parsed = parser.parse_args()
    # Buy command was given and now parsed
    if hasattr(parsed, "buy"):
        handleBuy(parsed)

    if hasattr(parsed, "sell"):
        # handleSell(parsed)
        print("command is SELL")
        print(parsed)


if __name__ == "__main__":
    main()
