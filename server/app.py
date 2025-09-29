from conn import DB
from flask import Flask, request, jsonify

app = Flask(__name__)

db = DB()

@app.route('/users', methods=['GET'])
def get_users():
    db.execute("SELECT * FROM users")
    users = db.fetchall()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')

    if not name or not password:
        return jsonify({"error": "Name and password are required"}), 400

    db.execute("INSERT INTO users (name, password) VALUES (?, ?)", (name, password))
    return jsonify({"message": "User added successfully"}), 201

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db.execute("DELETE FROM users WHERE id = ?", (user_id,))
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)