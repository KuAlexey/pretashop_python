import pytest
from abc import ABC


@pytest.mark.usefixtures('setup_driver')
class BaseTest(ABC):
    pass
