"""Analysis functions. Replace the starter function with your own."""
import numpy as np


def summary_stats(values):
    """Mean and sample standard deviation of a set of measurements.

    Parameters
    ----------
    values : array-like of float
        Measurements, all in the same units.

    Returns
    -------
    dict
        ``{"mean": ..., "std": ..., "n": ...}`` with mean and std in the input units.

    Raises
    ------
    ValueError
        If fewer than two values are given.
    """
    x = np.asarray(values, dtype=float)
    if x.size < 2:
        raise ValueError("Need at least two values")
    return {"mean": float(x.mean()), "std": float(x.std(ddof=1)), "n": int(x.size)}
