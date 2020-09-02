import log
import requests
import json
import pandas as pd

# from datetime import datetime

from backtestd.csv_loader import (
    load_csv_results,
    merge_csv_results,
    construct_accessible_csv_path,
    construct_accessible_csv_paths_list,
)

api_dict_keys = (
    'name',
    'date',
    'optimize',
    'optimize_crit',
    'backtest_model',
    'symbols',
    'visual',
    'store_results',
    'indi_set',
)


class Run:
    """A backtestd run"""

    # name
    # date
    # optimize
    # optimize_crit
    # backtest_model
    # symbols
    # visual
    # store_results
    # indi_set = {Indicator}

    def __init__(
        self,
        indi_set,
        name,
        date,
        optimize,
        optimize_crit,
        backtest_model,
        symbols,
        visual,
        store_results,
        parent=None,
    ):
        self.name = name
        self.date = date
        self.optimize = optimize
        self.optimize_crit = optimize_crit
        self.backtest_model = backtest_model
        self.symbols = symbols
        self.visual = visual
        self.store_results = store_results
        self.indi_set = indi_set
        self.parent = parent
        self.executed = False

    @classmethod
    def from_config(cls, indi_set, config):
        return cls(indi_set, **config)

    def __eq__(self, other):
        if not isinstance(other, Run):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.__dict__ == other.__dict__

    def exec(self, url):
        """execute the run by calling the backtestd REST API"""
        log.info("Executing run " + self.name + " at " + url)
        api_ret = self.__call_backtestd(url)
        log.debug("api returned " + str(api_ret))
        self.__load_csv_results_after_exec()  # TODO spawn separate thread for better pipelining in the queue
        self.__move_csv_results()
        self.__slice_results()
        self.executed = True
        # TODO rename dataframe columns

    def __slice_results(self):
        log.info("Slicing results for run " + self.name)
        # TODO
        # slice results
        # create a list of new runs
        # set self.parent
        pass

    def __call_backtestd(self, url):
        with requests.Session() as session:
            r = session.post(
                url + "/run",
                data=self.to_json(),
                headers={"content-type": "application/json"},
            )
            if r.ok:
                return r.json()
            else:
                raise ValueError("Status: {}".format(r.reason))

    def __load_csv_results_after_exec(self):
        results = []
        for sym in self.symbols:
            p = construct_accessible_csv_path(self.name + "_" + sym + ".csv")
            log.debug("trying to load csv results {}".format(p))
            if p.exists():
                res = load_csv_results(p)
                if isinstance(res, pd.DataFrame):
                    log.debug("loaded {} results from {}".format(len(res), p))
                    results.append(res)
        if len(results) == 0:
            log.error("no results loaded")
            # TODO exception?
        else:
            self.results = merge_csv_results(results)

    def __move_csv_results(self):
        for sym in self.symbols:
            p = construct_accessible_csv_path(self.name + "_" + sym + ".csv")
            if p.exists():
                # TODO
                pass

    def load_csv_results_from_path_list(self, csv_paths):
        """Load the csv results into a pandas Dataframe"""
        results = []
        for p in csv_paths:
            res = load_csv_results(p)
            results.append(res)
        self.results = merge_csv_results(results)

    def __rename_input_columns_in_results(self):
        True  # TODO rename if there is input_description set

    # def get_input_names(self):
    #     """get the names of the inputs """
    #     from backtestd.indicator import get_indi_set_input_names
    #     names = get_indi_set_input_names(self.indi_set)
    #     if names:
    #         return names
    #     return detect_input_columns_in_csv(self.results.columns)

    def to_dict(self):
        """Export the content of the class to a dict to be used for calling the API"""
        return {k: self.__dict__[k] for k in api_dict_keys}

    def to_json(self):
        from backtestd.utils import json_converter

        return json.dumps(self.to_dict(), default=json_converter)
