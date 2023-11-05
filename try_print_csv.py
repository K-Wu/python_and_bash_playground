if __name__ == "__main__":
    sample = '''GrdX,GrdY,GrdZ,BlkX,BlkY,BlkZ,Reg/Trd,StcSMem (MB),DymSMem (MB),Strm,Name
,,,,,,,,,13,[CUDA memcpy Host-to-Device]
,,,,,,,,,13,[CUDA memcpy Host-to-Device]
8,8,2,128,1,1,86,0.033,0.000,13,ampere_sgemm_32x32_sliced1x4_nn
8,16,1,32,16,1,44,0.000,0.000,13,"""void splitKreduce_kernel<(int)32, (int)16, int, float, float, float, float, (bool)1, (bool)0, (bool)0>(cublasSplitKParams<T6>, const T4 *, const T5 *, T5 *, const T6 *, const T6 *, const T7 *, const T4 *, T7 *, void *, long, T6 *, int *)"""
'''
    import csv

    # Alternatively, an opened file can be passed to csv.reader as argument
    csvreader = csv.reader(sample.split("\n"), delimiter=",")
    for line in csvreader:
        print("\t".join(line))
