from multiprocessing import Process, Queue
import log


class RunQueue(Process):
    """
    An execution queue
    """

    def __init__(self, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.queue = Queue()

    def send(self, run):
        self.queue.put(run)

    def run(self):
        while True:
            # TODO check for new indicator configs in fs and add to the top of the queue
            run = self.queue.get()
            log.info("got run " + run.name + " from the queue")
            try:
                run.exec(self.url)
            except ValueError as e:
                log.error(run.name + " failed ... skipping\n" + str(e))
