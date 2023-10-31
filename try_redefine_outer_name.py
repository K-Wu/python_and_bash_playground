NCU_DETAILS_COLUMN_IDX: "dict[str, int]" = {
    "ID": 0,
    "Kernel Name": 4,
    "Section Name": 11,
    "Metric Name": 12,
    "Metric Unit": 13,
    "Metric Value": 14,
    "Rule Name": 15,
    "Rule Type": 16,
    "Rule Description": 17,
}


def get_redefined():
    return {"id": 0, "kernel name": 4}


def redefine():
    NCU_DETAILS_COLUMN_IDX = get_redefined()
    print(NCU_DETAILS_COLUMN_IDX)


if __name__ == "__main__":
    print(NCU_DETAILS_COLUMN_IDX)
    redefine()
    print(NCU_DETAILS_COLUMN_IDX)
