import random


# "The canonical way to share information across modules within a single program is to create a special module (often called config or cfg)." https://docs.python.org/3/faq/programming.html#how-do-i-share-global-variables-across-modules
# Reference on how python caches modules so that they are only loaded once: https://docs.python.org/3/library/sys.html#sys.modules
global var
var = random.randint(0, 100)


# From https://github.com/inducer/pycuda/blob/5cb2e1a32f330c2984e2c1bf0579022494381ef1/pycuda/autoinit.py
def _finish_up():
    global var
    print("atexit tearing down: var is", var)
    var = None


import atexit

atexit.register(_finish_up)
