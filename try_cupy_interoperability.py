# Adapted from https://docs.cupy.dev/en/stable/user_guide/interoperability.html
# Adapted from https://docs.rapids.ai/api/kvikio/stable/quickstart/
def try_load_via_cufile():
    import cupy
    import kvikio

    path = "test-file"

    a = cupy.arange(100)
    f = kvikio.CuFile(path, "w")
    # Write whole array to file
    f.write(a)
    f.close()

    b = cupy.empty_like(a)
    f = kvikio.CuFile(path, "r")
    # Read whole array from file
    f.read(b)
    assert all(a == b)

    # Use contexmanager
    c = cupy.empty_like(a)
    with kvikio.CuFile(path, "r") as f:
        f.read(c)
    assert all(a == c)

    # Non-blocking read
    d = cupy.empty_like(a)
    with kvikio.CuFile(path, "r") as f:
        future1 = f.pread(d[:50])
        future2 = f.pread(d[50:], file_offset=d[:50].nbytes)
        future1.get()  # Wait for first read
        future2.get()  # Wait for second read
    assert all(a == d)


def try_cupy_interop():
    import cupy as cp
    import torch

    # convert a torch tensor to a cupy array
    a = torch.rand((4, 4), device="cuda")
    b = cp.asarray(a)
    b *= b

    # check the underlying memory pointer is the same
    assert (
        a.__cuda_array_interface__["data"][0]
        == b.__cuda_array_interface__["data"][0]
    )

    # convert a cupy array to a torch tensor
    a = cp.arange(10)
    b = torch.as_tensor(a, device="cuda")
    b += 3
    assert (
        a.__cuda_array_interface__["data"][0]
        == b.__cuda_array_interface__["data"][0]
    )


def try_load_torch_via_cufile():
    import cupy
    import kvikio
    import torch
    path = "test-file"

    a_t = torch.arange(100)
    a = cupy.asarray(a_t)
    f = kvikio.CuFile(path, "w")
    # Write whole array to file
    f.write(a)
    f.close()

    b_t = torch.empty_like(a_t)
    b = cupy.asarray(b_t)
    f = kvikio.CuFile(path, "r")
    # Read whole array from file
    f.read(b)
    assert all(a == b)

    # Use contexmanager
    c_t = torch.empty_like(a_t)
    c = cupy.asarray(c_t)
    with kvikio.CuFile(path, "r") as f:
        f.read(c)
    assert all(a == c)

    # Non-blocking read
    d_t = torch.empty_like(a_t)
    d = cupy.asarray(d_t)
    with kvikio.CuFile(path, "r") as f:
        future1 = f.pread(d[:50])
        future2 = f.pread(d[50:], file_offset=d[:50].nbytes)
        future1.get()  # Wait for first read
        future2.get()  # Wait for second read
    assert all(a == d)

    del a
    del b
    del c
    del d
    print(a_t, b_t, c_t, d_t)

print("Try cufile")
try_load_via_cufile()
print("Try cupy interop")
try_cupy_interop()
print("Try loading torch via cufile")
try_load_torch_via_cufile()