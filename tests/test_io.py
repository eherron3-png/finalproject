import pandas as pd
import pytest

from toolkit.io import load_data, validate


@pytest.fixture
def tiny_table():
    """A small hand-made table with the required columns."""
    return pd.DataFrame({"sample_id": ["A", "B", "C"], "value": [1.0, 2.0, 3.0]})


def test_load_data_reads_csv(tmp_path, tiny_table):
    path = tmp_path / "tiny.csv"
    tiny_table.to_csv(path, index=False)
    df = load_data(path)
    assert list(df.columns) == ["sample_id", "value"]
    assert len(df) == 3


def test_load_data_missing_file():
    with pytest.raises(FileNotFoundError):
        load_data("no_such_file.csv")


def test_validate_accepts_good_table(tiny_table):
    assert validate(tiny_table) is tiny_table


def test_validate_rejects_missing_column(tiny_table):
    with pytest.raises(ValueError, match="Missing required"):
        validate(tiny_table.drop(columns="value"))
