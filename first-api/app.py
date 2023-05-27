from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "O senhor dos anéis - A sociedade do Anel",
        "author": "J.R.R Tolkien"
    },
    {
        "id": 2,
        "title": "Harry Potter e a Pedra Filosofal",
        "author": "J.K Howling"
    },
    {
        "id": 3,
        "title": "Hábitos Atômicos",
        "author": "James Clear"
    },
]


@app.route("/books", methods=["GET"])
def get_all_books():
  return jsonify(books)


@app.route("/books", methods=["POST"])
def create_new_book():
  new_book = request.get_json()
  books.append(new_book)
  return books


@app.route("/books/<int:id>", methods=["GET"])
def get_unic_book(id):
  for book in books:
    if book.get("id") == id:
      return jsonify(book)


@app.route("/books/<int:id>", methods=["PUT"])
def edit_book_for_id(id):
  new_book = request.get_json()
  for index, book in enumerate(books):
    if (book.get("id") == id):
      books[index].update(new_book)
      return jsonify(books[index])


@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book_for_id(id):
  for index, book in enumerate(books):
    if book.get("id") == id:
      del books[index]
      return books


app.run(port=5000, host="localhost", debug=True)
