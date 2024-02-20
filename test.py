import pytest
from main import app, library,Book

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add_book(client):
    response = client.post('/add_book', json={"title": "Test Book", "author": "Test Author", "isbn": "987654321", "publication_year": 2022})
    assert response.status_code == 200
    assert "Book added successfully" in response.json['message']
    assert len(library.books) == 1

def test_borrow_book(client):
    # Add a book first
    test_book = {"title": "Test Book", "author": "Test Author", "isbn": "987654321", "publication_year": 2022}
    library.add_book(test_book)
    
    response_borrow = client.post('/borrow_book', json={"isbn": "987654321"})
    assert response_borrow.status_code == 200
    assert "Book borrowed successfully" in response_borrow.json['message']
    assert library.books[0].status == 'borrowed'

def test_return_book(client):
    # Add and borrow a book first
    test_book = {"title": "Test Book", "author": "Test Author", "isbn": "987654321", "publication_year": 2022}
    library.add_book(test_book)
    library.update_status("987654321", "borrowed")

    response_return = client.post('/return_book', json={"isbn": "987654321"})
    assert response_return.status_code == 200
    assert "Book returned successfully" in response_return.json['message']
    assert library.books[0].status == 'available'

def test_search_books(client):
    # Add a book for searching
    test_book = Book(title="Test Book", author="Test Author", isbn="987654321", publication_year=2022)
    library.add_book(test_book)

    response_search = client.get('/search_books?query=test')  # Change 'keyword' to 'query'
    assert response_search.status_code == 200
    assert len(response_search.json['results']) == 1
    assert response_search.json['results'][0]['title'] == 'Test Book'



def test_invalid_borrow(client):
    response = client.post('/borrow_book', json={"isbn": "123456789"})
    assert response.status_code == 404
    assert "Book not found or already borrowed" in response.json['error']

def test_invalid_return(client):
    response = client.post('/return_book', json={"isbn": "123456789"})
    assert response.status_code == 404
    assert "Book not found or already available" in response.json['error']

