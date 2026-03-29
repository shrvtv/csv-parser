import subprocess
from pathlib import Path

import pytest

from main import CSVParser


@pytest.fixture
def csv_parser():
    return CSVParser()


@pytest.fixture
def math_csv():
    return "tests/fixtures/math.csv"


@pytest.fixture
def physics_csv():
    return "tests/fixtures/physics.csv"


@pytest.fixture
def programming_csv():
    return "tests/fixtures/programming.csv"


def test_cli_output():
    result = subprocess.run(
        [
            "python3",
            "main.py",
            "--files",
            "tests/fixtures/physics.csv",
            "tests/fixtures/math.csv",
            "tests/fixtures/programming.csv",
            "--report",
            "None"
        ],
        capture_output=True,
        text=True
    )

    assert result.stdout == Path("tests/fixtures/expected.txt").read_text()


def test_read(csv_parser, math_csv):
    data = csv_parser.read(math_csv)
    assert len(data) == 45
    assert data[0] == {
        "student": "Алексей Смирнов",
        "date": "2024-06-01",
        "coffee_spent": "450",
        "sleep_hours": "4.5",
        "study_hours": "12",
        "mood": "норм",
        "exam": "Математика",
    }
