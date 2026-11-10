"""Load and validate the project's data."""
from pathlib import Path

import pandas as pd

# ✏️ Change to the columns your dataset must contain.
REQUIRED_COLUMNS = ["sample_id", "value"]


def load_data(path):
    """Load a CSV file into a DataFrame.

    Parameters
    ----------
    path : str or Path
        Path to a CSV file.

    Returns
    -------
    pandas.DataFrame
        The file's contents.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")
    return pd.read_csv(path)


def validate(df, required=REQUIRED_COLUMNS):
    """Check that a DataFrame has the required columns and is not empty.

    Parameters
    ----------
    df : pandas.DataFrame
        The data to check.
    required : list of str
        Column names that must be present.

    Returns
    -------
    pandas.DataFrame
        The same DataFrame, so calls can be chained.

    Raises
    ------
    ValueError
        If the table is empty or a required column is missing.
    """
    if df.empty:
        raise ValueError("The data table is empty")
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required column(s): {missing}")
    return df
