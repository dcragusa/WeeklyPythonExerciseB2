from solution import str_range


def test_same_start_end():
    r = str_range('a', 'a')
    assert iter(r) == r
    assert ''.join(list(r)) == 'a'


def test_simple():
    r = str_range('a', 'c')
    assert ''.join(list(r)) == 'abc'


def test_simple_with_step():
    r = str_range('a', 'c', 2)
    assert ''.join(list(r)) == 'ac'


def test_simple_with_negativestep():
    r = str_range('c', 'a', -2)
    assert ''.join(list(r)) == 'ca'


def test_hebrew():
    r = str_range('א', 'ז', 2)
    assert ''.join(list(r)) == 'אגהז'


test_same_start_end()
test_simple()
test_simple_with_step()
test_simple_with_negativestep()
test_hebrew()
