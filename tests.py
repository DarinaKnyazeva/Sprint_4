import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

        # напиши свои тесты ниже
        # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book("Гарри Поттер и Философский камень")
        collector.add_new_book("Гарри Поттер и Тайная комната")
        books = collector.get_books_genre()
        assert len(books) == 2

    @pytest.mark.parametrize("name, genre", [
        ("Властелин колец. Братство кольца", "Фантастика"),
        ("Король Лев", "Мультфильмы")
    ])
    def test_set_genre_book(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_genre_book(self, collector):
        collector.add_new_book("Убийство на улице Морг")
        collector.set_book_genre("Убийство на улице Морг", "Детективы")
        assert collector.get_book_genre("Убийство на улице Морг") == "Детективы"

    def test_check_added_have_no_genres_books(self, collector):
        names = ["1984", "Анна Каренина", "Маленькие женщины"]
        for book_name in names:
            collector.add_new_book(book_name)
            assert collector.get_book_genre(book_name) == ""

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Сияние")
        collector.set_book_genre("Сияние", "Ужасы")

        collector.add_new_book("ОНО")
        collector.set_book_genre("ОНО", "Ужасы")

        assert collector.get_books_with_specific_genre('Ужасы') == ['Сияние', 'ОНО']

    def test_get_genre_empty_books(self, collector):
        assert collector.get_books_genre() == {}

    def test_get_books_genre_with_books(self, collector):
        collector.add_new_book("Королевство слепых")
        collector.set_book_genre("Королевство слепых", "Детективы")

        collector.add_new_book("Двенадцать стульев")
        collector.set_book_genre("Двенадцать стульев", "Комедии")

        expected_genres = {
            "Королевство слепых": "Детективы",
            "Двенадцать стульев": "Комедии"
        }
        assert collector.get_books_genre() == expected_genres

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Кэрри")
        collector.set_book_genre("Кэрри", "Ужасы")

        collector.add_new_book("Корпорация монстров")
        collector.set_book_genre("Корпорация монстров", "Мультфильмы")

        children_books = collector.get_books_for_children()
        assert children_books == ["Корпорация монстров"]

    def test_delete_from_favorites_book(self, collector):
        collector.add_new_book("Бойцовский клуб")
        collector.add_book_in_favorites("Бойцовский клуб")
        collector.delete_book_from_favorites("Бойцовский клуб")
        favorites = collector.get_list_of_favorites_books()
        assert "Бойцовский клуб" not in favorites

    def test_get_list_of_favorites_books(self, collector):
        assert collector.get_list_of_favorites_books() == []

        collector.add_new_book("Искупление")
        collector.add_book_in_favorites("Искупление")
        assert "Искупление" in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize("name", [
        "Мастер и Маргарита",
        "Война и мир",
    ])
    def test_add_to_favorites(self, collector, name):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()
