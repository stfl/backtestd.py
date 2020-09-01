optimize = (
    'Disabled',   # = 0, // optimization disabled
    'Complete',   # = 1, // "Slow complete algorithm"
    'Genetic',    # = 2, // "Fast genetic based algorithm"
    'AllSymbols'  # = 3, // "All symbols selected in Market Watch"
)

optimize_crit = (
    'Balance',          # = 0,         // the maximum balance value,
    'BalanceProf',      # = 1,     // the maximum value of product of the balance and profitability,
    'BalancePayoff',    # = 2,   // the product of the balance and expected payoff,
    'Drawdown',         # = 3,        // the maximum value of the expression (100% - Drawdown)*Balance,
    'BalanceRecovery',  # = 4, // the product of the balance and the recovery factor,
    'BalanceSharpe',    # = 5,   // the product of the balance and the Sharpe Ratio,
    'Custom'            # = 6, // a custom optimization criterion received from the OnTester() function in the Expert Advisor).
)

backtest_model = (
    'EveryTick',      # = 0, Every tick
    'OneMinuteOHLC',  # = 1, 1 minute OHLC
    'OpenPrice',      # = 2, Open price only
    'MathCalc',       # = 3, Math calculations
    'EveryTickReal'   # = 4, Every tick based on real ticks
)

store_results = (
    'None',  # 0, // optimization disabled
    'SideChanges',  # 1, // "Slow complete algorithm"
    'Buffers',  # 2,     // "Fast genetic based algorithm"
    'Results',  # 3,     // "All symbols selected in Market Watch"
)

signal_class = (
    'Preset',  # 0,
    'ZeroLineCross',  # 1,
    'TwoLinesCross',  # 2,
    'TwoLinesTwoLevelsCross',  # 3,
    'TwoLevelsCross',  # 4,
    'PriceCross',  # 5,
    'PriceCrossInverted',  # 6,
    'Semaphore',  # 7,
    'TwoLinesColorChange',  # 8,
    'ColorChange',  # 9,
    'BothLinesTwoLevelsCross',  # 10,
    'BothLinesLevelCross',  # 11,
    'SaturationLevels',  # 12,
    'SaturationLines',  # 13,
    'BothLinesSaturationLevels',  # 14,
    'SlopeChange',  # 15,
    'TwoLinesSlopeChange',  # 16,
    )

funcs = ('Confirm',
         'Confirm2',
         'Confirm3',
         'Baseline',
         'Volume',
         'Exit',
         'Continue'
         )

funcs_short = ('C1', 'C2', 'C3', 'B', 'V', 'E', 'Ct')
