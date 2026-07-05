#Author: Marko Gvero
#Module 4 Lab - Case Study: Python APIs
#Filename: Module4-Lab-MarkoGvero.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model): #creates the class Book with the attributes id, book_name, author, and publisher
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    publisher = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"
    

@app.route('/')  #adds a route to the home page that returns a welcome message and the available routes
def home():
    return jsonify({
        "message": "Welcome to the Book Database API",
        "available_routes": [
            "/books",
            "/books/<id>"
        ]
    })

@app.route('/books')
def get_books(): #gets all the books in books.db and returns them in a JSON format
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
        
    return {"books": output}


@app.route('/books/<id>')
def get_book(id): #gets a specific book by its id and returns it in a JSON format
    book = Book.query.get_or_404(id)
    return jsonify({"book_name": book.book_name, "author": book.author, "publisher": book.publisher})



@app.route('/books', methods=['POST'])
def add_book(): #adds a new book to the books.db database using the data provided in the request body
    book = Book(book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return jsonify({"id": book.id})

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id): #deletes a specific book by its id from the books.db database
    book = Book.query.get(id)
    if book is None:
        return jsonify({"message": "Book not found"}), 404
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted"})



if __name__ == "__main__":
    with app.app_context():
        db.create_all() #creates the books.db database if it doesn't exist
    app.run(debug=True)
