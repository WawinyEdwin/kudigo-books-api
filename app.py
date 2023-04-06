from flask import Flask, jsonify, request
from flask_cors import CORS
from utils.db import (
    get_book_by_id,
    get_books,
    add_book,
    update_book_by_id,
    delete_book,
    create_books_table,
    delete_book_by_id
)

create_books_table()
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/api", methods=["GET"])
def api():
    return "Running"


@app.route("/books", methods=["GET"])
def list_books():
    return jsonify(get_books()), 200


@app.route("/books", methods=["POST"])
def create_book():
    book = request.get_json()
    created = add_book(book)
    if created is not None:
        return jsonify(created), 201

    return "failed to add book", 500


@app.route("/books/<book_id>", methods=["GET"])
def fetch_book(book_id):
    book = get_book_by_id(book_id)
    if book is not None:
        return jsonify(book), 200

    return "book not found", 404


@app.route("/books/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = request.get_json()
    updated = update_book_by_id(book, book_id)
    if updated is not None:
        return jsonify(updated), 200

    return "failed to updated book", 500


@app.route("/books/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    msg = delete_book_by_id(book_id)
    if msg is not None:
        return jsonify(msg), 204

    return "failed to delete book", 500


if __name__ == "__main__":
    app.run()
