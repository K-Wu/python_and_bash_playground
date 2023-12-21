import random

global var
var = random.randint(0, 100)


# From https://github.com/inducer/pycuda/blob/5cb2e1a32f330c2984e2c1bf0579022494381ef1/pycuda/autoinit.py
def _finish_up():
    global var
    print("atexit tearing down: var is", var)
    var = None


import atexit

atexit.register(_finish_up)
