# From https://stackoverflow.com/questions/50735493/how-to-share-a-list-of-tensors-in-pytorch-multiprocessing
import torch.multiprocessing as mp
import torch


def foo(q, worker, tl):
    tl[worker] += (worker + 1) * 1000
    if worker == 0:
        dummy = torch.randn(2, device="cuda:0")
        dummy.timestamp = (
            12345  # This property will not be passed to the other process
        )
        q.put((dummy, 12345))
    else:
        dummy, timestamp = q.get()
        print("dummy=", timestamp)


if __name__ == "__main__":
    mp.set_start_method("spawn", force=True)
    tl = [torch.randn(2, device="cuda:0"), torch.randn(3, device="cuda:0")]

    for t in tl:
        t.share_memory_()

    print("before mp: tl=")
    print(tl)

    q = mp.Queue()

    p0 = mp.Process(target=foo, args=(q, 0, tl))
    p1 = mp.Process(target=foo, args=(q, 1, tl))
    p0.start()
    p1.start()
    p0.join()
    p1.join()

    print("after mp: tl=")
    print(tl)
