from backtestd.run_queue import RunQueue
from backtestd.run import Run
from backtestd.enums import backtest_model, optimize, optimize_crit, store_results
from backtestd.csv_loader import construct_accessible_csv_path

import pytest
from datetime import datetime


def describe_queue():
    @pytest.fixture
    def remote_url():
        return "http://192.168.12.61:12311"

    @pytest.fixture
    def queue(remote_url):
        return RunQueue(remote_url)

    @pytest.fixture
    def run_config():
        return {
            'backtest_model': backtest_model.index('OpenPrice'),
            'date': [datetime(2018, 1, 1, 0, 0), datetime(2019, 1, 1, 0, 0)],
            'name': 'bt_run',
            'optimize': optimize.index('Complete'),
            'optimize_crit': optimize_crit.index('Custom'),
            'symbols': ['EURUSD'],
            'visual': False,
            'store_results': store_results.index('None'),
        }

    @pytest.fixture
    def indi_set():
        return {
            "Confirm": {
                'name': 'ash',
                'inputs': [[9.0, 8., 10., 1.], [2.0], [0.0], [0.0], [0.0]],
                'shift': 0,
                'buffers': [0],
                'class': 'ZeroLineCross',
                'filename': 'ASH',
            },
            "Exit": {
                'name': 'Rex',
                'inputs': [[14.0], [0.0], [14.0], [0.0],],
                'shift': 0,
                'buffers': [0, 1],
                'class': 'TwoLinesCross',
                'filename': 'Rex',
            },
            "Volume": {
                'name': 'volatility_ratio',
                'inputs': [[25.0], [0.0]],
                'shift': 0,
                'buffers': [0],
                'class': 'TwoLevelsCross',
                'filename': 'Volatility_ratio',
                'levels': [1.0, 1.0, 1.0, 1.0],
            },
        }

    @pytest.mark.skip(reason="testing remote API -> takes ages")
    def with_full_queue(queue, run_config, indi_set):
        queue.start()
        r = Run({'Confirm': indi_set['Confirm']}, **run_config)
        __rm_run_results_files(r)
        queue.send(r)

        r2 = Run({'Confirm': indi_set['Confirm']}, **run_config)
        r2.name = "bt_run2"
        r2.symbols = ['AUDCAD', 'GBPCHF']
        __rm_run_results_files(r2)
        queue.send(r2)
        queue.join()

def __rm_run_results_files(run):
    for sym in run.symbols:
        p = construct_accessible_csv_path(run.name + "_" + sym + ".csv")
        p.unlink(missing_ok=True)
