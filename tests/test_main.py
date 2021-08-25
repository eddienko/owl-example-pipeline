from unittest import mock

from distributed.utils_test import client  # noqa: F401

from owl_example_pipeline.main import main
from owl_example_pipeline.schema import schema


def test_schema():
    config = {"datalen": 100}
    schema(config)


@mock.patch("time.sleep", return_value=None)
def test_main(psleep):
    config = {"datalen": 10}
    main.config = {}
    res = main(**config)
    assert res == 120
