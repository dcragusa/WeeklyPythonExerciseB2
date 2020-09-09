from pathlib import Path
from hashlib import sha1
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


def get_single_file_info(filepath):
    if filepath.is_file():
        stats = filepath.stat()
        return {
            'path': str(filepath),
            'filename': filepath.name,
            'created': datetime.fromtimestamp(stats.st_ctime),
            'last_modified': datetime.fromtimestamp(stats.st_mtime),
            'last_accessed': datetime.fromtimestamp(stats.st_atime),
            'sha1': sha1(str.encode(filepath.read_text())).hexdigest(),
        }


def get_file_info(root):
    with ThreadPoolExecutor() as pool:
        return [i for i in pool.map(get_single_file_info, Path(root).rglob('*')) if i is not None]
