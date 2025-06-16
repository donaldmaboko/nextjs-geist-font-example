from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:19006", "http://localhost:8000"]}})

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({'status': 'running'})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    # Add authentication logic here
    return jsonify({'message': 'Login successful', 'user': data.get('username')})

@app.route('/api/book-ride', methods=['POST'])
def book_ride():
    data = request.json
    # Add ride booking logic here
    return jsonify({'message': 'Ride booked successfully', 'details': data})

if __name__ == '__main__':
    app.run(debug=True)
