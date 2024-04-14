import concurrent.futures
import torch
import time
import weakref


def print_after_sleep(t: torch.Tensor):
    print("sleeping")
    time.sleep(1)
    print("woke up", t)


if __name__ == "__main__":
    executor = concurrent.futures.ThreadPoolExecutor()
    t = torch.tensor([1, 2, 3])
    executor.submit(print_after_sleep, t)
    executor.submit(print_after_sleep, t)
    wr = weakref.ref(t)
    del t
    while True:
        time.sleep(1)
        print("main thread weakref", wr())
