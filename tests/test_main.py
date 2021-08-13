from unittest import mock

from distributed.utils_test import client  # noqa: F401

from owl_example_pipeline.main import main
from owl_example_pipeline.schema import schema


def test_schema():
    config = {"datalen": 100, "cpu_bound": False, "output_dir": "/tmp"}
    schema(config)


@mock.patch("time.sleep", return_value=None)
def test_main(psleep):
    config = {"datalen": 10, "cpu_bound": False, "output_dir": "/tmp"}
    main.config = {}
    res = main(**config)
    assert res == 120
