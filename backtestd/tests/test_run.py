"""Sample unit test module using pytest-describe and expecter."""
# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison
import pytest

from backtestd.run import Run
from backtestd.enums import backtest_model, optimize, optimize_crit, store_results
from datetime import datetime
from backtestd.tests.test_indicator import test_indis as indis


run_config = {'backtest_model': backtest_model.index('OpenPrice'),
              'date': [datetime(2018, 1, 1, 0, 0),
                       datetime(2019, 1, 1, 0, 0)],
              'name': 'bt_run',
              'optimize':      optimize.index('Complete'),
              'optimize_crit': optimize_crit.index('Custom'),
              'symbols': ['EURUSD'],
              'visual': False,
              'store_results': store_results.index('None')
              }


all_symbols = ['EURUSD', 'AUDCAD', 'GBPUSD', 'USDCHF', 'USDJPY', 'USDCAD',
               'AUDUSD', 'EURCHF', 'EURJPY', 'EURGBP', 'EURCAD', 'GBPCHF',
               'GBPJPY', 'AUDJPY', 'AUDNZD', 'AUDCHF', 'CHFJPY', 'EURAUD',
               'EURNZD', 'CADCHF', 'GBPAUD', 'GBPCAD', 'GBPNZD', 'NZDCAD',
               'NZDCHF', 'NZDJPY', 'NZDUSD', 'CADJPY'],

# pub struct Indicator {
#     pub name: String,
#     pub filename: Option<String>,
#     pub class: SignalClass,
#     pub inputs: Vec<Vec<BigDecimal>>,
#     pub buffers: Option<Vec<u8>>,
#     pub params: Option<Vec<BigDecimal>>,
#     pub shift: u8,
# }


def test_init():
    config = run_config
    r = Run(config, {"Confirm": indis[1], "Baseline": indis[2]})
    assert r


def test_to_dict():
    s = {"Confirm": indis[1], "Baseline": indis[2]}
    r = Run(run_config, s)
    assert r.to_dict() == {**run_config, "indi_set":  s}


def test_to_json():
    from pprint import pprint
    s = {"Confirm": indis[1], "Baseline": indis[5]}
    r = Run(run_config, s)
    pprint(r.to_json())


@pytest.mark.skip(reason="testing remote API -> takes ages")
def describe_call_backtestd():
    @pytest.fixture
    def run():
        return Run(run_config, {"Confirm":
                                {'name': 'ash',
                                 'inputs': [[9.0], [2.0], [0.0], [0.0], [0.0]],
                                 'shift': 0,
                                 'buffers': [0],
                                 'class': 'ZeroLineCross',
                                 'filename': 'ASH'},
                                })

    @pytest.fixture
    def remote_url():
        return "http://192.168.12.61:12311"

    def with_good_run(run, remote_url):
        ret = run._call_backtestd(remote_url)
        assert ret == ['reports\\bt_run_EURUSD.csv']

    # @pytest.mark.skip(reason="testing remote API -> takes ages")
    def with_bad_run(run, remote_url):
        run.optimize = 8
        with pytest.raises(ValueError):
            run._call_backtestd(remote_url)


# def describe_construct_csv_paths():
#     from pathlib import Path
#     from backtestd.run import __construct_accessible_csv_paths

#     @pytest.fixture
#     def workdir():
#         return Path("/mnt/workdir")
#     # workdir = Path("/mnt/workdir")

#     def with_windows_paths(workdir):
#         csv_results = ['reports\\bt_run_EURUSD.csv', 'reports\\bt_run_USDCHF.csv']
#         assert (__construct_accessible_csv_paths(workdir, csv_results) ==
#                 [Path('/mnt/workdir/reports/bt_run_EURUSD.csv'),
#                  Path('/mnt/workdir/reports/bt_run_USDCHF.csv')]
#                 )

#     def with_nested_windows_paths(workdir):
#         csv_results = ['path\\reports\\bt_run_USDCHF.csv']
#         assert (__construct_accessible_csv_paths(workdir, csv_results) ==
#                 [Path('/mnt/workdir/path/reports/bt_run_USDCHF.csv')]
#                 )

#     def with_unix_paths(workdir):
#         csv_results = ['reports/bt_run_EURUSD.csv', 'reports/bt_run_USDCHF.csv']
#         assert (__construct_accessible_csv_paths(workdir, csv_results) ==
#                 [Path('/mnt/workdir/reports/bt_run_EURUSD.csv'),
#                  Path('/mnt/workdir/reports/bt_run_USDCHF.csv')]
#                 )

#     def with_empty():
#         assert (__construct_accessible_csv_paths(workdir, []) == [])
