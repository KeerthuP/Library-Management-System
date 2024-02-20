from flask import Flask, request, jsonify
from models import Book, Library

app = Flask(__name__)

library=Library()

@app.route('/add_book', methods=['POST'])
def add_book():
    try:
        data = request.get_json()

        # Ensure that 'title', 'author', 'isbn', and 'publication_year' keys are present
        title = data['title']
        author = data['author']
        isbn = data['isbn']
        publication_year = data['publication_year']

        new_book = Book(title, author, isbn, publication_year)
        library.add_book(new_book)

        return jsonify({'message': 'Book added successfully'})
    except KeyError as e:
        return jsonify({'error': f'Missing required key: {e.args[0]}'})

@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    data = request.get_json()
    isbn = data.get('isbn', None)
    if library.update_status(isbn, 'borrowed'):
        return jsonify({'message': 'Book borrowed successfully'})
    else:
        return jsonify({'error': 'Book not found or already borrowed'})

@app.route('/return_book', methods=['POST'])
def return_book():
    data = request.get_json()
    isbn = data.get('isbn', None)
    if library.update_status(isbn, 'available'):
        return jsonify({'message': 'Book returned successfully'})
    else:
        return jsonify({'error': 'Book not found or not borrowed'})

@app.route('/search_books', methods=['GET'])
def search_books():
    query = request.args.get('query')
    results = [book.__dict__ for book in library.search_books(query)]
    return jsonify({'results': results})

if __name__=='__main__':
    app.run(debug=True)

