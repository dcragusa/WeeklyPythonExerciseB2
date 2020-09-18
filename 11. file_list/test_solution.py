from solution import FileInfo, FileList
import os.path
import shutil
from pathlib import Path


def test_empty_fileinfo():
    fi = FileInfo('filename', 'mtime', 'sha1')
    assert fi.filename == 'filename'
    assert fi.mtime == 'mtime'
    assert fi.sha1 == 'sha1'
    assert str(fi) == 'FileInfo for filename, mtime mtime, sha1 sha1'


def test_nothing(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()

    fl = FileList(d)

    assert len(fl.all_file_infos) == 0
    assert fl.all_file_infos == []


def test_three_good_files(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()

    for i in [1, 500, 1000]:
        with open(d / f'file{i}', 'w') as f:
            f.write('abcd\n' * i)

    assert len(list(d.iterdir())) == 3

    fl = FileList(d)
    fl.scan()
    assert type(fl.all_file_infos) == list
    assert len(fl.all_file_infos) == 3

    assert {'file1', 'file500', 'file1000'} == {os.path.basename(one_item.filename)
                                                for one_item in fl.all_file_infos}

    assert {'819abca7eabfd860df0d96b850cd43d64fce35c4',
            'e31780bcdeb62dfd8b939fa9b77dc7412cc83399',
            '3330b4373640f9e4604991e73c7e86bfd8da2dc3'} == {one_item.sha1
                                                            for one_item in fl.all_file_infos}

def test_rescan_do_nothing(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()

    for i in [1, 500, 1000]:
        with open(d / f'file{i}', 'w') as f:
            f.write('abcd\n' * i)

    assert len(list(d.iterdir())) == 3

    fl = FileList(d)
    fl.scan()

    rescan_output = fl.rescan()
    assert rescan_output['added'] == []
    assert rescan_output['removed'] == []
    assert rescan_output['changed'] == []


def test_rescan_add_file(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()

    for i in [1, 500, 1000]:
        with open(d / f'file{i}', 'w') as f:
            f.write('abcd\n' * i)

    assert len(list(d.iterdir())) == 3

    fl = FileList(d)
    fl.scan()

    with open(d / f'file9', 'w') as f:
        f.write('abcd\n' * 9)

    rescan_output = fl.rescan()

    assert rescan_output['removed'] == []
    assert rescan_output['changed'] == []

    assert len(rescan_output['added']) == 1
    assert os.path.basename(rescan_output['added'][0]) == 'file9'


def test_rescan_change_file(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()

    for i in [1, 500, 1000]:
        with open(d / f'file{i}', 'w') as f:
            f.write('abcd\n' * i)

    assert len(list(d.iterdir())) == 3

    fl = FileList(d)
    fl.scan()

    with open(d / f'file1', 'a') as f:
        f.write('efgh\n')

    rescan_output = fl.rescan()

    assert rescan_output['added'] == []
    assert rescan_output['removed'] == []

    assert len(rescan_output['changed']) == 1
    assert os.path.basename(rescan_output['changed'][0]) == 'file1'


def test_rescan_remove_file(tmp_path):
    d = tmp_path / 'sub'
    d.mkdir()

    for i in [1, 500, 1000]:
        with open(d / f'file{i}', 'w') as f:
            f.write('abcd\n' * i)

    assert len(list(d.iterdir())) == 3

    fl = FileList(d)
    fl.scan()

    (d / 'file1').unlink()

    rescan_output = fl.rescan()

    assert rescan_output['added'] == []
    assert rescan_output['changed'] == []

    assert len(rescan_output['removed']) == 1
    assert os.path.basename(rescan_output['removed'][0]) == 'file1'


if __name__ == '__main__':
    test_empty_fileinfo()
    for func in [
        test_nothing, test_three_good_files, test_rescan_do_nothing,
        test_rescan_add_file, test_rescan_change_file, test_rescan_remove_file
    ]:
        try:
            os.mkdir('temp')
            func(Path('temp'))
        finally:
            shutil.rmtree('temp')

