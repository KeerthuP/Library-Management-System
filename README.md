# Library-Management-System
This Book Library System is a simple application developed in Python using Flask and REST APIs.
It allows users to manage books, borrow, return, and search for books in a library.

## Getting Started
Set up and run the Book Library System on the local machine.

### Prerequisites
- Python 3.x (Visual Studio Code)
- Flask REST API
- POSTMAN
  
### Installation
1. **Create Virtual Environment:**

    python -m venv myEnv
  

2. **Activate Virtual Environment:**
   
  .\myEnv\Scripts\activate
      

3. **Install Dependencies:**

   pip install flask
 

### Running the Application

1. **Run the Flask Application:**
    python models.py
    python main.py

    I have used visual studio to code and the output * Running on http://127.0.0.1:5000

3. **Access the Application:**

   In web browser,(http://127.0.0.1:5000/) opens.

## API Endpoints in POSTMAN

- **Add Book:**
    - Endpoint: `http://127.0.0.1:5000/add_book`
    - Method: POST
    - RequestBody: JSON data
    {
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "123456789",
  "publication_year": 1925
}

- **Output**
- {
    "message": "Book added successfully"
}

- **Borrow Book:**
    - Endpoint: `http://127.0.0.1:5000/borrow_book`
    - Method: POST
    - RequestBody: JSON data
    - {
 "isbn": "123456789"
}
 -**Output**
{
    "message": "Book borrowed successfully"
}

- **Return Book:**
    - Endpoint: `http://127.0.0.1:5000/return_book`
    - Method: POST
    - RequestBody: JSON data
    - {
 "isbn": "123456789"
}
-**Output**
{
    "message": "Book returned successfully"
}

- **Search Books:**
    - Endpoint: `http://127.0.0.1:5000/search_books`
    - Method: GET
    - Query Parameter: http://127.0.0.1:5000/search_books?keyword=gatsby
 -**Output**
{
    "results": [
        {
            "author": "F. Scott Fitzgerald",
            "isbn": "123456789",
            "publication_year": 1925,
            "status": "available",
            "title": "The Great Gatsby"
        }
      
