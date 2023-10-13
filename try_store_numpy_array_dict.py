import numpy as np

data_to_store = {"a": np.array([1, 2, 3])}
np.savez("test.npz", **data_to_store)
data_loaded = dict(np.load("test.npz"))
print(data_loaded)
