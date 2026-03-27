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
    )
    parser.add_argument(
        "--report",
        help="specify the report filename",
    )

    args = parser.parse_args()


if __name__ == "__main__":
    main()
