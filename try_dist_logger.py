from .logger import logger
import logging
import torch

torch.distributed.init_process_group(backend="nccl", init_method="env://")
if torch.distributed.get_rank() == 0 or torch.distributed.get_rank() == 1:
    logger.setLevel(logging.getLevelName("INFO"))
else:
    logging.disable()

logger.info("This is an info message.")
