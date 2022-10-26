import random
import time
from pathlib import Path

from dask import delayed
from owl_dev import pipeline
from owl_dev.logging import logger


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
    time.sleep(random.random() * 10)
    return x + y


@pipeline
def main(*, datalen: int, input_path: Path: None, output_path: Path = None) -> int:  # pragma: no cover
    """Example pipeline.

    The pipeline constructs a list of ``datalen`` elements and
    performs a series of operations on them.

    Parameters
    ----------
    datalen
        Length of list to use.
    output_path
        Output path
    input_path
        Input path

    Returns
    -------
    result of operations
    """

    logger.info("Computing...")

    acc = []
    for x in range(datalen):
        a = inc(x)
        b = double(x)
        c = add(a, b)
        acc.append(c)

    total = delayed(sum)(acc)
    return total.compute()

