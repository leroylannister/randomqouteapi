from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

# Load quotes from environment variable
quotes = os.environ.get('QUOTES', '').split('|')

@app.route('/quote')
def get_random_quote():
    if not quotes:
        return jsonify({"error": "No quotes available"}), 404
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)