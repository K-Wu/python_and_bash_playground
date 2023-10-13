#!/usr/bin/env bash
# cppclean from https://github.com/myint/cppclean
cppclean --include-path=/home/kwu/anaconda3/envs/dev_dgl_torch_new/lib/python3.9/site-packages/torch/include/ --include-path=/home/kwu/anaconda3/envs/dev_dgl_torch_new/lib/python3.9/site-packages/torch/include/torch/csrc/api/include/ --include-path=/home/kwu/anaconda3/envs/dev_dgl_torch_new/include/python3.9/ --include-path=include/ --include-path=../third_party/cusplibrary/ --include-path=../third_party/libnpy/include --include-path=../third_party/cutlass/include --include-path=../third_party/sputnik --include-path=/usr/local/cuda-11/targets/x86_64-linux/include .
