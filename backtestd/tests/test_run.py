"""Sample unit test module using pytest-describe and expecter."""
# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned,singleton-comparison

from backtestd.run import Run
from backtestd.enums import backtest_model, optimize, optimize_crit
from datetime import datetime


run_config = {'backtest_model': backtest_model.index('OpenPrice'),
              'date': [datetime(2018, 1, 1, 0, 0),
                       datetime(2019, 12, 11, 0, 0)],
              'name': 'bt_run',
              'optimize':      optimize.index('Genetic'),
              'optimize_crit': optimize_crit.index('Balance'),
              'symbols': ['EURUSD', 'AUDCAD', 'GBPUSD', 'USDCHF', 'USDJPY', 'USDCAD',
                          'AUDUSD', 'EURCHF', 'EURJPY', 'EURGBP', 'EURCAD', 'GBPCHF',
                          'GBPJPY', 'AUDJPY', 'AUDNZD', 'AUDCHF', 'CHFJPY', 'EURAUD',
                          'EURNZD', 'CADCHF', 'GBPAUD', 'GBPCAD', 'GBPNZD', 'NZDCAD',
                          'NZDCHF', 'NZDJPY', 'NZDUSD', 'CADJPY'],
              'visual': False
              }


# pub struct Indicator {
#     pub name: String,
#     pub filename: Option<String>,
#     pub class: SignalClass,
#     pub inputs: Vec<Vec<BigDecimal>>,
#     pub buffers: Option<Vec<u8>>,
#     pub params: Option<Vec<BigDecimal>>,
#     pub shift: u8,
# }

indis = {1: {'name': 'ALF2_baseline',
             'inputs': [[0.0, 5.0, 19.0, 2.0],
                        [10.0, 4.0, 24.0, 2.0],
                        [0.5, 0.1, 1.5, 0.2],
                        [0.0, 0.0, 21.0, 1.0]],
             'shift': 0,
             'buffers': [0],
             'class': 'PriceCross',
             'filename': 'Adaptive_Laguerre_filter_2',
             },
         2: {'name': 'Amka_baseline',
             'inputs': [[9.0, 5.0, 15.0, 1.0],
                        [2.0, 2.0, 8.0, 1.0],
                        [30.0, 20.0, 40.0, 2.0],
                        [2.0, 1.0, 3.0, 0.2]],
             'shift': 0,
             'buffers': [0],
             'class': 'PriceCross',
             'filename': 'amka-indicator',
             },
         3: {'name': 'Corr_avg_baseline',
             'inputs': [[0.0, 5.0, 19.0, 2.0],
                        [1.0, 0.0, 3.0, 1.0],
                        [14.0, 6.0, 24.0, 2.0],
                        [0.0, 0.0, 21.0, 1.0],
                        [0.0, 0.0, 1.0, 0.1],
                        [3.0],
                        [25.0, 15.0, 35.0, 2.0],
                        [90.0, 75.0, 95.0, 5.0],
                        [10.0, 5.0, 25.0, 5.0]],
             'shift': 0,
             'buffers': [5],
             'class': 'PriceCross',
             'filename': 'Corr_average',
             },
         4: {'name': 'GMA',
             'inputs': [[-1.0], [21.0, 9.0, 35.0, 2.0]],
             'shift': 0,
             'buffers': [1],
             'class': 'PriceCross',
             'filename': 'YGMA',
             },
         5: {'name': 'kijunsen',
             'inputs': [[9.0], [26.0, 6.0, 60.0, 1.0], [52.0]],
             'shift': 0,
             'class': 'Preset',
             },
         6: {'name': 'ma',
             'inputs': [[18.0, 40.0, 2.0], [0.0], [0.0, 3.0, 1.0], [0.0, 6.0, 1.0]],
             'shift': 0,
             'class': 'Preset',
             },
         7: {'name': 'Plombiers',
             'inputs': [[145.0, 35.0, 200.0, 20.0],
                        [2.0, 0.0, 4.0, 1.0],
                        [0.0],
                        [0.0],
                        [2.1415, 1.1415, 3.2, 0.2],
                        [1.0],
                        [1.0],
                        [21.0, 14.0, 27.0, 2.0],
                        [7.0, 3.0, 12.0, 2.0],
                        [9.0, 5.0, 15.0, 1.0],
                        [0.0, 0.0, 3.0, 1.0],
                        [0.0, 0.0, 1.0, 1.0],
                        [-99.0, -199.0, 0.0, 50.0]],
             'shift': 0,
             'buffers': [5],
             'class': 'PriceCrossInverted',
             'filename': 'plombiers-indicator',
             },
         8: {'name': 'QWMA_baseline',
             'inputs': [[0.0, 5.0, 19.0, 2.0],
                        [25.0, 15.0, 35.0, 2.0],
                        [2.0, 0.0, 10.0, 0.5],
                        [0.0, 0.0, 21.0, 1.0],
                        [0.0, -1.0, 1.0, 1.0],
                        [3.0],
                        [25.0, 15.0, 35.0, 2.0],
                        [90.0, 75.0, 95.0, 5.0],
                        [10.0, 5.0, 25.0, 5.0]],
             'shift': 0,
             'buffers': [4],
             'class': 'PriceCross',
             'filename': 'QWMA_ca',
             },
         9: {'name': 'YMA',
             'inputs': [[21.0, 9.0, 35.0, 2.0], [-1.0]],
             'shift': 0,
             'buffers': [0],
             'class': 'PriceCross',
             'filename': 'YGMA',
             }}


def test_init():
    config = run_config
    r = Run(config, {"Confirm": indis[1], "Baseline": indis[2]})
    assert r


def test_init():
    config = run_config
    r = Run(config, {"Confirm": indis[1], "Baseline": indis[2]})
    assert r
