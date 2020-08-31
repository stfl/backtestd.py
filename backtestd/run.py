import log


class Run:
    """A backtestd run"""

    def __init__(self, config, indi_set):
        self.__dict__ = config
        self.indi_set = indi_set

    def exec(self):
        """execute the run by calling the backtestd REST API"""
        log.debug("Executing run")
        True

    # def _call_backtestd(self):
    # with requests.Session() as session:
    #     r = session.post(url + "/run",
    #                       data=json.dumps(run, default = json_converter),
    #                       headers={"content-type": "application/json"})
    #     if r.ok:
    #         return r.json()
    #     else:
    #         raise ValueError("Status: {}".format(r.reason))

    def load_csv_results(self):
        """Load the csv results into a pandas Dataframe"""
        True

    def to_dict(self):
        """Export the content of the class to a dict to be used for calling the API"""
        True

    @classmethod
    def from_indi_desc_file(cls):
        True

    @classmethod
    def from_indi_desc(cls):
        True




