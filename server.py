from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

books = []

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    books.append(data)
    return jsonify({"message": "Buku ditambahkan", "data": data}), 201

@app.route('/books/<int:index>', methods=['PUT'])
def update_book(index):
    if index < len(books):
        data = request.get_json()
        books[index] = data
        return jsonify({"message": "Buku diperbarui", "data": data})
    return jsonify({"error": "Index tidak valid"}), 404

@app.route('/books/<int:index>', methods=['DELETE'])
def delete_book(index):
    if index < len(books):
        deleted = books.pop(index)
        return jsonify({"message": "Buku dihapus", "data": deleted})
    return jsonify({"error": "Index tidak valid"}), 404

if __name__ == '__main__':
    app.run(debug=True)
