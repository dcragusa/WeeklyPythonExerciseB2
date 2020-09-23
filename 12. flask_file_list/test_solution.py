import shutil
from solution import app, BASE_DIR

app.config.update({'TESTING': True})
client = app.test_client()


def test_no_dir_supplied():
    response = client.get('/scan').get_json()
    assert 'Error' in response


def test_dir_does_not_exist():
    response = client.get('/scan?directory=test').get_json()
    assert 'Error' in response


def test_empty_dir():
    d = BASE_DIR / 'test'
    d.mkdir()

    response = client.get('/scan?directory=test').get_json()
    assert response == []

    shutil.rmtree(d)


def test_dir():
    d = BASE_DIR / 'test'
    d.mkdir()
    (d / '1.txt').touch()
    (d / '2.txt').touch()

    response = client.get('/scan?directory=test').get_json()
    assert response == ['1.txt', '2.txt']

    shutil.rmtree(d)


test_no_dir_supplied()
test_dir_does_not_exist()
test_empty_dir()
test_dir()


