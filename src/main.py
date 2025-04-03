# filepath: /csv-analysis/csv-analysis/src/main.py

from flask import Flask, request, jsonify, render_template
from utils.file_handler import read_file
from analyzer.csv_analyzer import CsvAnalyzer
import os

app = Flask(__name__)

# Ensure the upload folder exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', error='No file selected')
    
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', error='No file selected')
    
    if not file.filename.endswith('.csv'):
        return render_template('index.html', error='Please upload a CSV file')

    try:
        data = read_file(file)
        analyzer = CsvAnalyzer()
        analysis_result = analyzer.analyze_data(data)
        return render_template('index.html', result=analysis_result)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)