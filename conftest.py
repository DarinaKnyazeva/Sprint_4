import pytest

from main import BooksCollector

@pytest.fixture
def collector_books():
    return BooksCollector()