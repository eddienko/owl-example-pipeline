import logging
import random
import time
from pathlib import Path

from dask import delayed


logger = logging.getLogger("owl.daemon.pipeline")


@delayed
def inc(x):  # pragma: no cover
    time.sleep(random.random() * 10)
    return x + 1


@delayed
def double(x):  # pragma: no cover
    time.sleep(random.random() * 10)
    return x + 2


@delayed
def add(x, y):  # pragma: no cover
    logger.info("Adding....")
    time.sleep(random.random() * 10)
    return x + y


def main(*, datalen: int, output_dir: Path=None) -> int:  # pragma: no cover
    """Example pipeline.

    The pipeline constructs a list of ``datalen`` elements and
    performs a series of operations on them.

    Parameters
    ----------
    datalen
        Length of list to use.

    Returns
    -------
    result of operations
    """

    logger.info("Computing...")

    output = []
    for x in range(datalen):
        a = inc(x)
        b = double(x)
        c = add(a, b)
        output.append(c)

    total = delayed(sum)(output)
    return total.compute()

