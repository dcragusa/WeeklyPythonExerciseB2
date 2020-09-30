import shutil
from solution import app, BASE_DIR

app.config.update({'TESTING': True})
client = app.test_client()


def test_no_scan_dir_supplied():
    response = client.get('/scan').get_json()
    assert 'Error' in response


def test_scan_dir_does_not_exist():
    response = client.get('/scan?directory=test').get_json()
    assert 'Error' in response


def test_empty_scan_dir():
    d = BASE_DIR / 'test'
    d.mkdir()

    response = client.get('/scan?directory=test').get_json()
    assert response == []

    shutil.rmtree(d)


def test_scan():
    d = BASE_DIR / 'test'
    d.mkdir()
    (d / '1.txt').touch()
    (d / '2.txt').touch()

    response = client.get('/scan?directory=test').get_json()
    assert response == ['1.txt', '2.txt']

    shutil.rmtree(d)


def test_no_rescan_dir_supplied():
    response = client.get('/rescan').get_json()
    assert 'Error' in response


def test_rescan_dir_does_not_exist():
    response = client.get('/rescan?directory=test').get_json()
    assert 'Error' in response


def test_rescan_without_scan():
    d = BASE_DIR / 'test2'
    d.mkdir()

    response = client.get('/rescan?directory=test2').get_json()
    assert 'Error' in response

    shutil.rmtree(d)


def test_rescan():
    d = BASE_DIR / 'test2'
    d.mkdir()
    (d / '1.txt').touch()
    (d / '2.txt').touch()

    client.get('/scan?directory=test2').get_json()

    (d / '1.txt').unlink()
    (d / '3.txt').touch()
    with open(d / '2.txt', 'w') as f:
        f.write('spam')

    response = client.get('/rescan?directory=test2').get_json()

    assert response == {'added': ['3.txt'], 'changed': ['2.txt'], 'removed': ['1.txt']}

    shutil.rmtree(d)


test_no_scan_dir_supplied()
test_scan_dir_does_not_exist()
test_empty_scan_dir()
test_scan()

test_no_rescan_dir_supplied()
test_rescan_dir_does_not_exist()
test_rescan_without_scan()
test_rescan()
