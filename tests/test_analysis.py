import pytest

from toolkit.analysis import summary_stats


def test_summary_stats_known_answer():
    # Hand-computed: values 2, 4, 6 -> mean 4, sample std 2
    result = summary_stats([2, 4, 6])
    assert result["mean"] == 4
    assert result["std"] == pytest.approx(2.0)
    assert result["n"] == 3


def test_summary_stats_tolerance():
    # 0.1 + 0.2 is not exactly 0.3 in floating point, so compare with a tolerance
    assert summary_stats([0.1, 0.2])["mean"] == pytest.approx(0.15)


def test_summary_stats_rejects_one_value():
    with pytest.raises(ValueError):
        summary_stats([5.0])
