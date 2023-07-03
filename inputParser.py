import argparse
from datetime import datetime


def create_parser():
    parser = argparse.ArgumentParser(description="Grocery store",
                                     prog="SuperPy",
                                     usage="SuperPy [buy]")

    # basic_commands
    commands = parser.add_subparsers(
        metavar="Subcommands",
        title="SuperPy",
        help="Use [subcommand] -h to get extra info on usage",
    )

    # buy_commands
    buy = commands.add_parser(
        "buy",
        help="action for buying an item.",
    )
    buy.add_argument(
        "buy",
        action="store_true",
        default=False
    )
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
        help="supply the price of the product to buy EURO",
        required=True,
    )
    buy.add_argument(
        "--amount",
        "-a",
        metavar="PRODUCT_AMOUNT",
        type=int,
        default=1,
        help="supply the amount of product purchased (default=1)",
    )
    buy.add_argument(
        "--expiration",
        "-e",
        metavar="EXPIRATION dd/mm/yyyy'",
        type=lambda s: datetime.strptime(s, "%d/%m/%Y"),
        help="supply the expiration date of product dd/mm/yyyy",
        required=True,
    )

    # sell_commands
    sell = commands.add_parser(
        "sell",
        help="action for selling an item.",
    )
    sell.add_argument(
        "sell",
        action="store_true",
        default=False
    )
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
        help="supply the price of the product to sell",
        required=True,
    )
    sell.add_argument(
        "--amount",
        "-a",
        metavar="PRODUCT_AMOUNT",
        type=int,
        default=1,
        help="supply the amount of products to sell (default=1)",
    )

    # advance day instruction
    advance = commands.add_parser(
        "advance-time",
        help="Advance day by X days (default=1)",
    )
    advance.add_argument(
        "advance",
        action="store_true",
        default=False
    )
    advance.add_argument(
        '-d',
        metavar="DAYS",
        type=int,
        help="Advance day by given input days",
        required=True,
    )

    # report_commands
    report = commands.add_parser(
        "report",
        help="Produce reports",
    )
    report.add_argument(
        "report",
        action="store_true",
        default=False
    )

    # sub_reports
    reportSubcommands = report.add_subparsers(
        metavar="Subcommands",
        title="Report",
        help="Use [subcommand] -h to get extra info",
    )

    # inventory_report
    inventory = reportSubcommands.add_parser(
        "inventory", help="Returns inventory"
    )
    inventory.add_argument(
        "inventory",
        action="store_true",
        default=False,
        help="Returns current inventory"
    )
    inventory.add_argument(
        "--today",
        "-t",
        action="store_true",
        default=False,
        help="Returns inventory for today."
    )
    inventory.add_argument(
        "--yesterday",
        "-y",
        action="store_true",
        default=False,
        help="Returns inventory for yesterday.",
    )
    inventory.add_argument(
        "--now",
        "-n",
        action="store_true",
        default=False,
        help="Returns inventory for now (given day by advance-time input)",
    )
    inventory.add_argument(
        "--date",
        "-d",
        metavar="DATE_INPUT_INVENTORY",
        type=lambda s: datetime.strptime(s, "%d/%m/%Y"),
        help="Returns inventory for input-date",
    )

    # revenue_report
    revenue = reportSubcommands.add_parser(
        "revenue", help="Returns revenue"
    )
    revenue.add_argument(
        "revenue",
        action="store_true",
        default=False,
        help="Returns current revenue"
    )
    revenue.add_argument(
        "--today",
        "-t",
        action="store_true",
        default=False,
        help="Returns revenue for today."
    )
    revenue.add_argument(
        "--yesterday",
        "-y",
        action="store_true",
        default=False,
        help="Returns revenue for yesterday.",
    )
    revenue.add_argument(
        "--now",
        "-n",
        action="store_true",
        default=False,
        help="Returns revenue for now (given day by advance-time input)",
    )
    revenue.add_argument(
        "--date",
        "-d",
        metavar="DATE_INPUT_REVENUE",
        type=lambda s: datetime.strptime(s, "%d/%m/%Y"),
        help="Returns revenue for input-date",
    )
    revenue.add_argument(
        "--startingdate",
        "-s",
        metavar="DATE_INPUT_REVENUE",
        type=lambda s: datetime.strptime(s, "%d/%m/%Y"),
        help="Returns revenue from input-date to current-date",
    )

    # profit_report
    profit = reportSubcommands.add_parser(
        "profit", help="Returns profit"
    )
    profit.add_argument(
        "profit",
        action="store_true",
        default=False,
        help="Returns current profit"
    )
    profit.add_argument(
        "--today",
        "-t",
        action="store_true",
        default=False,
        help="Returns profit for today."
    )
    profit.add_argument(
        "--yesterday",
        "-y",
        action="store_true",
        default=False,
        help="Returns profit for yesterday.",
    )
    profit.add_argument(
        "--now",
        "-n",
        action="store_true",
        default=False,
        help="Returns profit for now (given day by advance-time input)",
    )

    profit.add_argument(
        "--date",
        "-d",
        metavar="DATE_INPUT_PROFIT",
        type=lambda s: datetime.strptime(s, "%d/%m/%Y"),
        help="Returns profit for input-date",
    )
    profit.add_argument(
        "--startingdate",
        "-s",
        metavar="DATE_INPUT_REVENUE",
        type=lambda s: datetime.strptime(s, "%d/%m/%Y"),
        help="Returns profit from input-date to currentdate",
    )

    return parser
