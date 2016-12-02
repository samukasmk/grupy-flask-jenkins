import pytest
from app import app as created_app

@pytest.fixture
def app():
    return created_app
