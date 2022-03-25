import BookShelf from '../src/iterator/bookshelf.mjs';
import Book from '../src/iterator/book.mjs';

const BOOKS = [
  'Around the World in 80 Days',
  'Bible',
  'Cinderella',
  'Daddy-Long-Legs',
];

describe('iterator', () => {
  it('bookshelf', () => {
    const shelf = new BookShelf(BOOKS.length);
    for (let i = 0, max = BOOKS.length; i < max; i += 1) {
      shelf.appendBook(new Book(BOOKS[i]));
    }

    let count = 0;
    const bookshelfIter = shelf.iterator();
    while (bookshelfIter.hasNext()) {
      const bk = bookshelfIter.next();

      expect(bk.title).toBe(BOOKS[count]);
      count += 1;
    }
  });
});