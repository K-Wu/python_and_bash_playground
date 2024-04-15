from recordclass import dataobject
import torch
import typing


class TensorEqID(dataobject):
    data_ptr: int
    dtype: torch.dtype
    size: int
    stride: tuple[int, ...]

    @classmethod
    def from_tensor(cls, tensor: torch.Tensor):
        return cls(
            data_ptr=tensor.untyped_storage().data_ptr(),
            dtype=tensor.dtype,
            size=tensor.untyped_storage().size(),
            stride=tensor.stride(),
        )

    def __str__(self):
        stride_str = "_".join(map(str, self.stride))
        return f"{self.data_ptr:x}_{self.dtype}_{self.size}_{stride_str}"


if __name__ == "__main__":
    a = torch.randn(5, 5, requires_grad=True)
    a_eqid = TensorEqID(
        a.untyped_storage().data_ptr(),
        a.dtype,
        a.untyped_storage().size(),
        a.stride(),
    )
    a_eqid_clone = TensorEqID(
        a.untyped_storage().data_ptr(),
        a.dtype,
        a.untyped_storage().size(),
        a.stride(),
    )
    print(isinstance(TensorEqID, typing.Hashable))
    print(a_eqid)
    print(a_eqid == a_eqid_clone)
    a_eqid_clone.size = 0
    print(a_eqid == a_eqid_clone)
    print(a_eqid == TensorEqID.from_tensor(a))
