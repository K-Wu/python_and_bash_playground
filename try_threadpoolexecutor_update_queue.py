import concurrent.futures
import time
import threading

lock = threading.Lock()


def async_task(
    job_being_done: dict[int, concurrent.futures.Future], job_id: int
):
    print(f"Job {job_id} done")
    with lock:
        del job_being_done[job_id]


class UselessJobQueue:
    job_being_done: dict[int, concurrent.futures.Future]
    executor: concurrent.futures.ThreadPoolExecutor

    def __init__(self):
        self.job_being_done = {}
        self.executor = concurrent.futures.ThreadPoolExecutor()

    def __del__(self):
        self.executor.shutdown()

    def add_job(self, job_id: int):
        with lock:
            self.job_being_done[job_id] = self.executor.submit(
                async_task, self.job_being_done, job_id
            )


if __name__ == "__main__":
    queue = UselessJobQueue()
    queue.add_job(1)
    queue.add_job(2)
    queue.add_job(3)

    while queue.job_being_done:
        time.sleep(1)
        print("Waiting...", queue.job_being_done)
