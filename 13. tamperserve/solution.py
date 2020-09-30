import os
import pickle
from pathlib import Path
from hashlib import sha1
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, jsonify

app = Flask(__name__)

BASE_DIR = Path(r'C:\temp')
ILLEGAL_CHARS = '/' if os.name == 'posix' else r'<>:"/\|?*'


class FileInfo:
    def __init__(self, filename, mtime, sha_1):
        self.filename, self.mtime, self.sha1 = filename, mtime, sha_1

    def __str__(self):
        return f'FileInfo for {self.filename}, mtime {self.mtime}, sha1 {self.sha1}'

    def __repr__(self):
        return f'FileInfo({self.filename}, {self.mtime}, {self.sha1})'


def get_single_file_info(filepath):
    if filepath.is_file():
        return FileInfo(
            filepath.name,
            datetime.fromtimestamp(filepath.stat().st_mtime),
            sha1(str.encode(filepath.read_text())).hexdigest()
        )


def scan_dir(directory):
    with ThreadPoolExecutor() as pool:
        return [
            i for i in pool.map(get_single_file_info, Path(directory).glob('*'))
            if i is not None
        ]


def get_pickle_name(directory):
    for char in ILLEGAL_CHARS:
        directory = directory.replace(char, '-')
    return directory + '.pkl'


@app.route('/scan')
def scan():
    if 'directory' not in request.args:
        return jsonify({'Error': 'You must supply a directory to scan.'}), 400
    sub_dir = request.args['directory']
    directory = BASE_DIR / sub_dir
    if not Path.is_dir(directory):
        return jsonify({'Error': 'Directory does not exist.'}), 400
    file_list = scan_dir(directory)
    with open(get_pickle_name(str(directory)), 'wb') as f:
        pickle.dump(file_list, f)
    return jsonify([file.filename for file in file_list]), 200


@app.route('/rescan')
def rescan():
    if 'directory' not in request.args:
        return jsonify({'Error': 'You must supply a directory to rescan.'}), 400
    sub_dir = request.args['directory']
    directory = BASE_DIR / sub_dir
    if not Path.is_dir(directory):
        return jsonify({'Error': 'Directory does not exist.'}), 400

    pickle_name = get_pickle_name(str(directory))
    if not os.path.isfile(pickle_name):
        return jsonify({'Error': 'Directory must be scanned before being rescanned.'}), 400
    with open(pickle_name, 'rb') as f:
        old_file_list = pickle.load(f)

    new_file_list = scan_dir(directory)

    with open(get_pickle_name(str(directory)), 'wb') as f:
        pickle.dump(new_file_list, f)

    names_old = {file.filename for file in old_file_list}
    names_new = {file.filename for file in new_file_list}
    modified_old = {(file.filename, file.sha1) for file in old_file_list}
    modified_new = {(file.filename, file.sha1) for file in new_file_list}
    added = names_new-names_old
    removed = names_old-names_new
    changed = {file[0] for file in modified_new-modified_old} - added

    return jsonify({'added': list(added), 'removed': list(removed), 'changed': list(changed)}), 200
