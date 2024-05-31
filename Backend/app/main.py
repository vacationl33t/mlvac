from flask import Flask, render_template, send_from_directory, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    static_dir = os.path.join(app.root_path, 'static')
    return send_from_directory(static_dir, filename)


@app.route('/query/', methods=['POST'])
def query():
    data = request.get_json()
    text = data.get('text')
    # Используйте имя сервиса вместо localhost
    ml_service_url = 'http://model:8000/query/'
    response = requests.post(ml_service_url, json={
        'text': text,
    })
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
