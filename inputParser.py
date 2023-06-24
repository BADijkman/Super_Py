import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="Grocery store",
                                     prog="SuperPy",
                                     usage="SuperPy [buy]")

    # basic_commands
    commands = parser.add_subparsers(
        metavar="Subcommands",
        title="SuperPy",
        help="Use [subcommand] -h to get extra info on usage of each subcommand",
    )

    # buy_commands
    buy = commands.add_parser(
        "buy",
        help="action for buying an item.",
    )

    buy.add_argument("buy", action="store_true",
                     default=False)

    buy.add_argument(
        "--name",
        "-n",
        metavar="PRODUCT_NAME",
        help="supply product name for the product to buy",
        required=True,
    )
    buy.add_argument(
        "--price",
        "-p",
        metavar="PRODUCT_PRICE",
        type=float,
        help="supply the price of the product",
        required=True,
    )
    buy.add_argument(
        "--amount",
        "-a",
        metavar="PRODUCT_AMOUNT",
        type=int,
        default=1,
        help="supply the amount of products purchased (default=1)",
    )

    buy.add_argument(
        "--expiration",
        "-e",
        metavar="EXPIRATION",
        help="supply the expiration date of products",
        required=True,
    )

    # sell_commands
    sell = commands.add_parser(
        "sell",
        help="action for selling an item.",
    )

    sell.add_argument("sell", action="store_true",
                      default=False)

    sell.add_argument(
        "--name",
        "-n",

        metavar="PRODUCT_NAME",
        help="supply product name for the product to sell",
        required=True,
    )
    sell.add_argument(
        "--price",
        "-p",
        metavar="PRODUCT_PRICE",
        type=float,
        help="supply the price of the product",
        required=True,
    )

    sell.add_argument(
        "--amount",
        "-a",
        metavar="PRODUCT_AMOUNT",
        type=int,
        default=1,
        help="supply the amount of products sold (default=1)",
    )
    return parser
