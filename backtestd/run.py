import log
import requests
import json
# from datetime import datetime

_api_dict_keys = ('name',
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

    def __init__(self, config, indi_set):
        self.__dict__ = config
        self.indi_set = indi_set

    def exec(self, url):
        """execute the run by calling the backtestd REST API"""
        log.debug("Executing run at " + url)
        csv_paths = self._call_backtestd(url)
        self.load_csv_results(csv_paths)

    def _call_backtestd(self, url):
        with requests.Session() as session:
            r = session.post(url + "/run",
                             data=self._to_json(),
                             headers={"content-type": "application/json"},
                             # timeout=0.2
                             )
            if r.ok:
                return r.json()
            else:
                raise ValueError("Status: {}".format(r.reason))

    def load_csv_results(self, csv_paths):
        """Load the csv results into a pandas Dataframe"""
        True

    def _to_dict(self):
        """Export the content of the class to a dict to be used for calling the API"""
        return {k: self.__dict__[k] for k in _api_dict_keys}

    def _to_json(self):
        from backtestd.utils import json_converter
        return json.dumps(self._to_dict(), default=json_converter)

    @classmethod
    def from_indi_desc_file(cls):
        True

    @classmethod
    def from_indi_desc(cls):
        True


def construct_accessible_csv_paths(mounted_workdir, csv_results):
    from pathlib import Path
    return [mounted_workdir / Path(r) for r in csv_results]
