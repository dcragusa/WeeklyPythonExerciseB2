from pathlib import Path
from hashlib import sha1
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


class FileInfo:
    def __init__(self, filename, mtime, sha_1):
        self.filename, self.mtime, self.sha1 = filename, mtime, sha_1

    def __str__(self):
        return f'FileInfo for {self.filename}, mtime {self.mtime}, sha1 {self.sha1}'

    def __repr__(self):
        return f'FileInfo({self.filename}, {self.mtime}, {self.sha1})'


class FileList:
    def __init__(self, directory):
        self.directory = directory
        self.last_scanned = None
        self.all_file_infos = self.scan()

    @staticmethod
    def get_single_file_info(filepath):
        if filepath.is_file():
            return FileInfo(
                filepath.name,
                datetime.fromtimestamp(filepath.stat().st_mtime),
                sha1(str.encode(filepath.read_text())).hexdigest()
            )

    def scan(self):
        with ThreadPoolExecutor() as pool:
            filepaths = [
                i for i in pool.map(self.get_single_file_info, Path(self.directory).glob('*'))
                if i is not None
            ]
        self.last_scanned = datetime.now()
        return filepaths

    def rescan(self):
        rescanned = self.scan()
        self.last_scanned = datetime.now()

        names_old = {file.filename for file in self.all_file_infos}
        names_new = {file.filename for file in rescanned}
        modified_old = {(file.filename, file.sha1) for file in self.all_file_infos}
        modified_new = {(file.filename, file.sha1) for file in rescanned}

        added = names_new-names_old
        removed = names_old-names_new
        changed = {file[0] for file in modified_new-modified_old} - added

        self.all_file_infos = rescanned
        return {'added': list(added), 'removed': list(removed), 'changed': list(changed)}
