from typing import NamedTuple

_WeightVar = NamedTuple("WeightVar", [("name", str), ("slice_type", str)])


class WeightVar(_WeightVar): ...


class WeightVarSpec(WeightVar):
    flag: bool
    ...


if __name__ == "__main__":
    spec = WeightVar(name="w1", slice_type="dense")
    print(spec)
