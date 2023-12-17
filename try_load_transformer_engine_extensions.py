# This file demonstrates that the dynamic library loading in another module, i.e., try_load_libc10, will be discovered automatically by the subsequent dynamic library in this module, which depends on the former dynamic library, loading in this module.

import try_load_libc10

import ctypes

transformer_engine_extensions_so = ctypes.CDLL(
    "/home/kwu/anaconda3/envs/dev_cupy_graph/lib/python3.11/site-packages/transformer_engine_extensions.cpython-311-x86_64-linux-gnu.so"
)
