import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Ensure each test runs with a clean copy of in-memory activity data."""
    original_state = copy.deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(original_state)
