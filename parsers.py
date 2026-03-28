import csv, itertools


def read_csv(filename: str) -> list[dict[str, str]]:
    with open(filename) as csvfile:
        return list(csv.DictReader(csvfile))


def merge_csv_files(filenames: list[str]) -> list[dict[str, str]]:
    return list(itertools.chain.from_iterable(map(read_csv, filenames)))


def csv_parser(
        filenames: list[str],
        formula: str,
        column: str
) -> list[dict[str, str]]:
    dataset = merge_csv_files(filenames)
    return dataset
