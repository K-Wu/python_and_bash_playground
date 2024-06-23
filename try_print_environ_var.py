"""If you use torchrun, all the processes will be affected by the environment variable set before the call. The following is an exemplary output of the script when run with torchrun:
❯ export MY_ENV_VAR=1234
❯ torchrun --nproc_per_node=2  /home/kwu/HET/hrt/misc/playground/try_print_environ_var.py
[2024-06-22 22:10:46,068] torch.distributed.run: [WARNING] 
[2024-06-22 22:10:46,068] torch.distributed.run: [WARNING] *****************************************
[2024-06-22 22:10:46,068] torch.distributed.run: [WARNING] Setting OMP_NUM_THREADS environment variable for each process to be 1 in default, to avoid your system being overloaded, please further tune the variable for optimal performance in your application as needed. 
[2024-06-22 22:10:46,068] torch.distributed.run: [WARNING] *****************************************
MY_ENV_VAR=1234
MY_ENV_VAR=1234
"""

import os

if "MY_ENV_VAR" in os.environ:
    print(f"MY_ENV_VAR={os.environ['MY_ENV_VAR']}")
else:
    print("MY_ENV_VAR not found in os.environ")
