import pytest

from app import run


@pytest.fixture()
def test_client():
    app = run.app
    return app.test_client()
