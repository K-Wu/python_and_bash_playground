import tqdm
import logging
from tqdm.contrib.logging import logging_redirect_tqdm
import time

NUM_SAMPLES = 10000
NUM_TILINGS = 5
LOG = logging.getLogger(__name__)

logging.basicConfig(
    format=(
        "%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d]"
        " %(threadName)15s: %(message)s"
    ),
    datefmt="%Y-%m-%d:%H:%M:%S",
    level=logging.INFO,
)

pbar = tqdm.tqdm(
    total=NUM_SAMPLES * NUM_TILINGS, ncols=0
)  # Suppress tqdm progress bar, and only print the progress stats
t0 = time.time()
with logging_redirect_tqdm():
    for idx in range(NUM_SAMPLES * NUM_TILINGS):
        pbar.update(1)
        time.sleep(0.0001)
        if idx % 1000 == 0:
            LOG.info("idx: %d", idx)


pbar.close()
LOG.info(
    "%d datapoints generated in %.2fs",
    NUM_SAMPLES * NUM_TILINGS,
    (time.time() - t0),
)
