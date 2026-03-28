import csv
import itertools
import statistics

from collections import defaultdict


class CSVParser:
    @staticmethod
    def read(filename: str) -> list[dict[str, str]]:
        with open(filename) as csvfile:
            return list(csv.DictReader(csvfile))

    def merge_files(self, filenames: list[str]) -> list[dict[str, str]]:
        return list(itertools.chain.from_iterable(map(self.read, filenames)))

    @staticmethod
    def filter_columns(
        dataset: list[dict[str, str]], columns = list[str]
    ) -> list[dict[str, str]]:
        return [
            {k: v for k, v in line.items() if k in columns} for line in dataset
        ]

    @staticmethod
    def group_by_column_into_dict(
        dataset: list[dict[str, str]], column_k: str, column_v: str
    ) -> defaultdict[str, list[float]]:
        result = defaultdict(list)
        if len(dataset[0]) != 2:
            raise ValueError("Unsupported dataset dimensions")

        for line in dataset:
            result[line[column_k]].append(float(line[column_v]))
        return result

    def parse(
        self, filenames: list[str], formula: str, columns: list[str]
    ) -> list[tuple[str, str]]:
        match formula:
            case "median":
                func = statistics.median
            case _:
                raise ValueError("Unsupported formula provided")
        dataset = self.merge_files(filenames)
        filtered_dataset = self.filter_columns(dataset, columns)
        grouped_by_first_column = self.group_by_column_into_dict(
            filtered_dataset,
            columns[0],
            columns[1]
        )
        applied_func_to_values = {
            k: str(int(func(v))) for k, v in grouped_by_first_column.items()
        }
        converted_from_dict_to_tuples = applied_func_to_values.items()
        sorted_down_by_second_column = sorted(
            converted_from_dict_to_tuples, key=lambda t: t[1], reverse=True
        )
        return sorted_down_by_second_column
