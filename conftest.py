import pytest
from main import BooksCollector

@pytest.fixture
def books_collector():
    """Фикстура для создания экземпляра BooksCollector."""
    return BooksCollector()
