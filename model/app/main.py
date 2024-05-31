from flask import Flask, request, jsonify
from flask_cors import CORS

from sys import platform

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

if platform == "linux" or platform == "linux2":
    from .model import gen_text

elif platform == "win32":
    from model import gen_text


@app.route('/query/', methods=['POST'])
def query():
    data = request.get_json()
    text = data.get('text')
    response = gen_text(text)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)