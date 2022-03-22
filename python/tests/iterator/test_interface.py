import pytest

from src.iterator.models import Book, BookShelf, ExtendableBookShelf

BOOKS = [
    "Around the World in 80 Days",
    "Bible",
    "Cinderella",
    "Daddy-Long-Legs",
]


class TestInterface:
    def test_bookshelf(self):
        bookshelf = BookShelf(len(BOOKS))
        for book in BOOKS:
            bookshelf.append_book(Book(name=book))

        count = 0
        bookshelf_iter = bookshelf.iterator()
        while bookshelf_iter.has_next():
            book = bookshelf_iter.next()
            assert book.name == BOOKS[count]
            count += 1

    @pytest.mark.parametrize("maxsize", [0, 1])
    def test_bookshelf_value_error(self, maxsize):
        bookshelf_holds_nothing = BookShelf(maxsize)
        for i in range(maxsize):
            bookshelf_holds_nothing.append_book(Book(name=f"{BOOKS[i]}"))

        with pytest.raises(ValueError):
            bookshelf_holds_nothing.append_book(Book(name=f"{BOOKS[maxsize]}"))

    def test_extendable_bookshelf(self):
        bookshelf = ExtendableBookShelf()
        for book in BOOKS:
            bookshelf.append_book(Book(name=book))

        count = 0
        bookshelf_iter = bookshelf.iterator()
        while bookshelf_iter.has_next():
            book = bookshelf_iter.next()
            assert book.name == BOOKS[count]
            count += 1