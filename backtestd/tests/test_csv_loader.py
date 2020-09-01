"""Sample unit test module using pytest-describe and expecter."""
# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

# import pytest

from backtestd.csv_loader import (
    load_csv_results,
    merge_csv_results
)

def test_load_csv_results():
    res = load_csv_results('backtestd/tests/files/ash_EURUSD.csv')
    assert len(res) == 10472


def describe_merge_csv_results():
    def with_single_file():
        res_list = [load_csv_results('backtestd/tests/files/ash_EURUSD.csv')]
        merged = merge_csv_results(res_list)
        assert "HitMiss" in merged
        assert len(merged) == 10472

    def with_multipe_files():
        res_list = [load_csv_results('backtestd/tests/files/ash_EURUSD.csv'),
                    load_csv_results('backtestd/tests/files/ash_AUDCAD.csv')]
        merged = merge_csv_results(res_list)
        assert "HitMiss" in merged
        assert len(merged) == 10472
