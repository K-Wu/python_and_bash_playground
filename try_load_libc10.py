import ctypes


# CUSPARSELT_SO = ctypes.cdll.LoadLibrary(
#     "/home/kwu/Downloads/libcusparse_lt-linux-x86_64-0.4.0.7-archive/lib/libcusparseLt.so"  # , mode=ctypes.RTLD_GLOBAL
# )
# CUSPARSELT_SO.sm80_xmma_sparse_gemm_i8i8_i8i32_f32_tn_n_tilesize128x64x128_stage4_warpsize2x2x1_sptensor16x8x64_execute_split_k_kernel_cusparse


# NVBLAS_SO = ctypes.CDLL(
#     "/usr/local/cuda-12/lib64/libnvblas.so"  # , mode=ctypes.RTLD_GLOBAL
# )


c10_so = ctypes.CDLL(
    "/home/kwu/anaconda3/envs/dev_cupy_graph/lib/python3.11/site-packages/torch/lib/libc10.so"
)
torch_cpu_so = ctypes.CDLL(
    "/home/kwu/anaconda3/envs/dev_cupy_graph/lib/python3.11/site-packages/torch/lib/libtorch_cpu.so"
)
