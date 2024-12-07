import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    """Создаёт экземпляр BooksCollector для каждого теста."""
    return BooksCollector()


def test_add_new_book_success(collector):
    collector.add_new_book("Гарри Поттер")
    assert "Гарри Поттер" in collector.get_books_genre()
    assert collector.get_book_genre("Гарри Поттер") == ""


def test_add_new_book_failure_due_to_long_name(collector):
    long_name = "А" * 41
    collector.add_new_book(long_name)
    assert long_name not in collector.get_books_genre()


def test_add_new_book_failure_due_to_duplicate(collector):
    collector.add_new_book("Гарри Поттер")
    collector.add_new_book("Гарри Поттер")
    assert len(collector.get_books_genre()) == 1


@pytest.mark.parametrize(
    "book, genre, expected",
    [
        ("Гарри Поттер", "Фантастика", "Фантастика"),
        ("Гарри Поттер", "Ужасы", "Ужасы"),
        ("Гарри Поттер", "Романтика", ""),  # Жанр отсутствует в списке
    ],
)
def test_set_book_genre(collector, book, genre, expected):
    collector.add_new_book(book)
    collector.set_book_genre(book, genre)
    assert collector.get_book_genre(book) == expected


def test_get_books_with_specific_genre(collector):
    collector.add_new_book("Гарри Поттер")
    collector.add_new_book("Сумерки")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    collector.set_book_genre("Сумерки", "Ужасы")
    assert collector.get_books_with_specific_genre("Фантастика") == ["Гарри Поттер"]
    assert collector.get_books_with_specific_genre("Ужасы") == ["Сумерки"]


def test_get_books_for_children(collector):
    collector.add_new_book("Гарри Поттер")
    collector.add_new_book("Дракула")
    collector.set_book_genre("Гарри Поттер", "Фантастика")
    collector.set_book_genre("Дракула", "Ужасы")
    assert collector.get_books_for_children() == ["Гарри Поттер"]


def test_add_book_in_favorites_success(collector):
    collector.add_new_book("Гарри Поттер")
    collector.add_book_in_favorites("Гарри Поттер")
    assert collector.get_list_of_favorites_books() == ["Гарри Поттер"]


def test_add_book_in_favorites_failure_due_to_absence(collector):
    collector.add_book_in_favorites("Неизвестная книга")
    assert collector.get_list_of_favorites_books() == []


def test_delete_book_from_favorites(collector):
    collector.add_new_book("Гарри Поттер")
    collector.add_book_in_favorites("Гарри Поттер")
    collector.delete_book_from_favorites("Гарри Поттер")
    assert collector.get_list_of_favorites_books() == []


def test_get_list_of_favorites_books(collector):
    collector.add_new_book("Гарри Поттер")
    collector.add_new_book("Сумерки")
    collector.add_book_in_favorites("Гарри Поттер")
    collector.add_book_in_favorites("Сумерки")
    assert collector.get_list_of_favorites_books() == ["Гарри Поттер", "Сумерки"]
