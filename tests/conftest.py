"""
Pytest configuration and fixtures.
"""

import os
import tempfile
from typing import Generator

import pytest


@pytest.fixture(autouse=True)
def clean_env() -> Generator[None, None, None]:
    """Clean environment variables before each test."""
    old_env = os.environ.pop("PIM_DATA_PATH", None)
    yield
    if old_env:
        os.environ["PIM_DATA_PATH"] = old_env
    else:
        os.environ.pop("PIM_DATA_PATH", None)
