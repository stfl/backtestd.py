import log


class Run:
    """A backtestd run"""

    def exec(self):
        """execute the run by calling the backtestd REST API"""
        log.debug("Executing run")
        True

    def load_csv_results(self):
        """Load the csv results into a pandas Dataframe"""
        True
