from solution import Foo, Uniquish


def test_foo():
    f1 = Foo(10)
    f2 = Foo(10)
    f3 = Foo(10)

    s = {f1, f2, f3}

    assert len(s) == 1
    assert hash(f1) == hash(f2)
    assert hash(f2) == hash(f3)


def test_subclass_non_uniquish():
    class Bar():
        def __init__(self, x):
            self.x = x

    b1 = Bar(10)
    b2 = Bar(10)
    b3 = Bar(10)

    s = {b1, b2, b3}

    assert len(s) == 3
    assert hash(b1) != hash(b2)
    assert hash(b2) != hash(b3)


def test_subclass_uniquish():
    class Bar(Uniquish):
        def __init__(self, x):
            self.x = x

    b1 = Bar(10)
    b2 = Bar(10)
    b3 = Bar(10)

    s = {b1, b2, b3}

    assert len(s) == 1
    assert hash(b1) == hash(b2)
    assert hash(b2) == hash(b3)


def test_uniquish_unhashable():
    class Bar(Uniquish):
        def __init__(self, x, y):
            self.x, self.y = x, y

    b1 = Bar(10, [1])
    b2 = Bar(10, [1])
    b3 = Bar(10, [2])

    s = {b1, b2, b3}

    assert len(s) == 2


test_foo()
test_subclass_non_uniquish()
test_subclass_uniquish()
test_uniquish_unhashable()
