import subprocess
from pathlib import Path


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
