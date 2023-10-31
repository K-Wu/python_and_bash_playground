"""This script tests if the type checker could work with pandera. From https://stackoverflow.com/a/76076231.
"""

import pandas as pd
import pandera as pa
from pandera.typing import DataFrame


class MySchema(pa.DataFrameModel):
    a: int
    b: float
    c: str = pa.Field(nullable=True)  # For example, allow None values
    d: float  # US dollars


class OtherSchema(pa.DataFrameModel):
    year: int = pa.Field(ge=1900, le=2050)


def generate_data() -> DataFrame[MySchema]:
    df = pd.DataFrame(
        {
            "a": [1, 2, 3],
            "b": [10.0, 20.0, 30.0],
            "c": ["A", "B", "C"],
            "d": [0.1, 0.2, 0.3],
        }
    )

    # Runtime verification here, throws on schema mismatch
    strongly_typed_df = DataFrame[MySchema](df)
    return strongly_typed_df


def transform(input: DataFrame[MySchema]) -> DataFrame[OtherSchema]:
    # This demonstrates that you can use strongly
    # typed column names from the schema
    df = input.filter(items=[MySchema.a]).rename(
        columns={MySchema.a: OtherSchema.year}
    )

    return DataFrame[OtherSchema](df)  # This will throw on range validation!


df1 = generate_data()
df2 = transform(df1)
transform(df2)  # mypy prints error here - incompatible type!
