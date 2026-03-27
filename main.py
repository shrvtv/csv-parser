#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Parses CSV files and forms a report"
    )
    parser.add_argument(
        "--files",
        nargs="+",
        help="specify the files to parse",
        required=True,
    )
    parser.add_argument(
        "--report",
        help="specify the report filename",
    )
    parser.add_argument(
        "-f", "--formula",
        help="select the math formula to use",
        choices=["median"],
        default="median",
    )
    parser.add_argument(
        "-c", "--column",
        help="specify the column name",
        default="coffee_spent"
    )

    args = parser.parse_args()


if __name__ == "__main__":
    main()
