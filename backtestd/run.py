import log
import requests
import json
# from datetime import datetime

from backtestd.csv_loader import (load_csv_results,
                                  merge_csv_results,
                                  construct_accessible_csv_path,
                                  construct_accessible_csv_paths_list)

api_dict_keys = ('name',
                   'date',
                   'optimize',
                   'optimize_crit',
                   'backtest_model',
                   'symbols',
                   'visual',
                   'indi_set',
                   'store_results',
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

    def __init__(self, config, indi_set):
        self.__dict__ = config
        self.indi_set = indi_set

    def exec(self, url):
        """execute the run by calling the backtestd REST API"""
        log.debug("Executing run at " + url)
        csv_paths = self.__call_backtestd(url)
        # mounted_csv_paths = construct_accessible_csv_paths(MOUNTED_WORKDIR, csv_paths)
        self.import_csv_results()
        # TODO rename dataframe columns

    def __call_backtestd(self, url):
        with requests.Session() as session:
            r = session.post(url + "/run",
                             data=self._to_json(),
                             headers={"content-type": "application/json"},
                             )
            if r.ok:
                return r.json()
            else:
                raise ValueError("Status: {}".format(r.reason))

    def import_csv_results(self):
        results = []
        for sym in self.symbols:
            p = construct_accessible_csv_path(self.name + "_" + sym + ".csv")
            if p.exists():
                res = load_csv_results(p)
                results.append(res)
        self.results = merge_csv_results(results)

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
