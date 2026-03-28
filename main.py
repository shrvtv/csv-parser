#!/usr/bin/env python3
import argparse
from tabulate import tabulate

from parsers import CSVParser


def main():
    argument_parser = argparse.ArgumentParser(
        description="Parses CSV files and forms a report"
    )
    argument_parser.add_argument(
        "--files",
        nargs="+",
        help="specify the files to parse",
        required=True,
    )
    argument_parser.add_argument(
        "--report",
        help="specify the report filename",
    )
    argument_parser.add_argument(
        "-f", "--formula",
        help="select the math formula to use",
        choices=["median"],
        default="median",
    )
    argument_parser.add_argument(
        "-c", "--column",
        help="specify the column name",
        default="coffee_spent"
    )

    args = argument_parser.parse_args()
    csv_parser = CSVParser()
    result = csv_parser.parse(args.files, args.formula, args.column)
    print(tabulate(result, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()
