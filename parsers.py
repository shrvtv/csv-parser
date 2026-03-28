import csv, itertools, statistics


class CSVParser:
    def read(self, filename: str) -> list[dict[str, str]]:
        with open(filename) as csvfile:
            return list(csv.DictReader(csvfile))

    def merge_files(self, filenames: list[str]) -> list[dict[str, str]]:
        return list(itertools.chain.from_iterable(map(self.read, filenames)))

    def filter_columns(
            self,
            dataset: list[dict[str, str]],
            columns = list[str]
    ) -> list[dict[str, str]]:
        pass

    def parse(
            self,
            filenames: list[str],
            formula: str,
            column: str
    ) -> list[dict[str, str]]:
        match formula:
            case "median":
                func = statistics.median
            case _:
                raise ValueError("Unsupported formula provided")
        dataset = self.merge_files(filenames)

        return dataset
