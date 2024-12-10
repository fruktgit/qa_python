import pytest

@pytest.mark.parametrize("book_name", ["Гарри Поттер", "Война и мир", "Детектив 1"])
def test_add_new_book_valid(books_collector, book_name):
    """Проверка добавления книг с валидным названием."""
    books_collector.add_new_book(book_name)
    assert book_name in books_collector.books_genre

@pytest.mark.parametrize("book_name", ["", "a" * 41])
def test_add_new_book_invalid(books_collector, book_name):
    """Проверка невозможности добавления книги с невалидным названием."""
    books_collector.add_new_book(book_name)
    assert book_name not in books_collector.books_genre

@pytest.mark.parametrize("genre", ["Фантастика", "Мультфильмы"])
def test_set_book_genre_valid(books_collector, genre):
    """Проверка установки валидного жанра."""
    books_collector.add_new_book("Гарри Поттер")
    books_collector.set_book_genre("Гарри Поттер", genre)
    assert books_collector.get_book_genre("Гарри Поттер") == genre

@pytest.mark.parametrize("genre", ["Роман", "Поэзия"])
def test_set_book_genre_invalid(books_collector, genre):
    """Проверка невозможности установки невалидного жанра."""
    books_collector.add_new_book("Гарри Поттер")
    books_collector.set_book_genre("Гарри Поттер", genre)
    assert books_collector.get_book_genre("Гарри Поттер") == ""

@pytest.mark.parametrize(
    "genre,expected_books",
    [
        ("Фантастика", ["Гарри Поттер"]),
        ("Мультфильмы", []),
    ]
)
def test_get_books_with_specific_genre(books_collector, genre, expected_books):
    """Проверка получения списка книг с определённым жанром."""
    books_collector.add_new_book("Гарри Поттер")
    books_collector.set_book_genre("Гарри Поттер", "Фантастика")
    assert books_collector.get_books_with_specific_genre(genre) == expected_books

def test_get_books_for_children(books_collector):
    """Проверка получения списка книг, подходящих детям."""
    books_collector.add_new_book("Гарри Поттер")
    books_collector.set_book_genre("Гарри Поттер", "Фантастика")
    books_collector.add_new_book("Детектив 1")
    books_collector.set_book_genre("Детектив 1", "Детективы")
    assert books_collector.get_books_for_children() == ["Гарри Поттер"]

def test_add_book_in_favorites_success(books_collector):
    """Проверка успешного добавления книги в избранное."""
    books_collector.add_new_book("Гарри Поттер")
    books_collector.add_book_in_favorites("Гарри Поттер")
    assert books_collector.get_list_of_favorites_books() == ["Гарри Поттер"]

def test_add_book_in_favorites_duplicate(books_collector):
    """Проверка невозможности повторного добавления книги в избранное."""
    books_collector.add_new_book("Гарри Поттер")
    books_collector.add_book_in_favorites("Гарри Поттер")
    books_collector.add_book_in_favorites("Гарри Поттер")
    assert len(books_collector.get_list_of_favorites_books()) == 1

def test_delete_book_from_favorites(books_collector):
    """Проверка успешного удаления книги из избранного."""
    books_collector.add_new_book("Гарри Поттер")
    books_collector.add_book_in_favorites("Гарри Поттер")
    books_collector.delete_book_from_favorites("Гарри Поттер")
    assert books_collector.get_list_of_favorites_books() == []
