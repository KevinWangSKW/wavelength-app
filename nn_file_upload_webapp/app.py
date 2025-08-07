from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
from model import predict_image

app = Flask(__name__, static_url_path='', static_folder='.')

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    prediction = predict_image(filepath)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)