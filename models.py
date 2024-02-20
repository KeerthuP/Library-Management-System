class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.status = 'available'

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def update_status(self, isbn, new_status):
        for book in self.books:
            print(f"Type of book: {type(book)}")
            print(f"Content of book: {book}")
            if book.isbn == isbn:
                book.status = new_status
                return True
        return False

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def search_books(self, query):
        results = []
        query = query.lower() if query else ""  # Convert to lowercase if not None
        for book in self.books:
            if (
                query in book.title.lower() if book.title else ""
                or query in book.author.lower() if book.author else ""
                or query in str(book.publication_year)
            ):
                results.append({
                'title': book.title,
                'author': book.author,
                'isbn': book.isbn,
                'publication_year': book.publication_year,
                'status': book.status
            })
        return results
