from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
  {
    'id': 1,
    'title': 'Lord of the Ring: The Fellowship of the Ring',
    'author': 'J.R.R. Tolkien',
  },
  {
    'id': 2,
    'title': 'Lord of the Ring: The Two Towers',
    'author': 'J.R.R. Tolkien',
  },
  {
    'id': 3,
    'title': 'Lord of the Ring: The Return of the King',
    'author': 'J.R.R. Tolkien',
  },
  {
    'id': 4,
    'title': 'The Hobbit',
    'author': 'J.R.R. Tolkien',
  },
]

@app.route('/books', methods=['GET'] )
def list_books():
  return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def find_book(id):
  for book in books:
    if book.get('id') == id:
      return jsonify(book)

@app.route('/books/<int:id>', methods=['PUT'])
def edit_books(id):
  edited_book = request.get_json()
  for index, book in enumerate(books):
    if book.get('id') == id:
      books[index].update(edited_book)
      return jsonify(books[index])
    
@app.route('/books', methods=['POST'])
def add_book():
  new_book = request.get_json()
  books.append(new_book)
  return jsonify(books)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
  for index, book in enumerate(books):
    if book.get('id') == id:
      del books[index]
      return jsonify(books)
    
    
app.run(port=5000,host='localhost',debug=True)
