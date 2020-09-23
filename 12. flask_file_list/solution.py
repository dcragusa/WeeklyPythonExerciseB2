from pathlib import Path
from flask import Flask, request, jsonify

app = Flask(__name__)

BASE_DIR = Path(r'C:\temp')


@app.route('/scan', methods=('GET', 'POST'))
def scan():
    if 'directory' not in request.args:
        return jsonify({'Error': 'You must supply a directory to scan.'})
    sub_dir = request.args['directory']
    directory = BASE_DIR / sub_dir
    if not Path.is_dir(directory):
        return jsonify({'Error': 'Directory does not exist.'})
    file_list = [str(path.name) for path in Path(directory).glob('*')]
    return jsonify(file_list)
