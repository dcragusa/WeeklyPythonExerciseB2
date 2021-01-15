import pytest
from solution import betterrepr


def replacement_str(self):
    return f'Replacement str, vars = {vars(self)}'


def replacement_repr(self):
    return f'Replacement repr, vars = {vars(self)}'


def test_one_attribute_default():
    @betterrepr()
    class Foo():
        def __init__(self, x):
            self.x = x

    f = Foo(10)
    assert str(f) == """Instance of Foo, vars = {'x': 10}"""


def test_two_attributes_default():
    @betterrepr()
    class Foo():
        def __init__(self, x, y):
            self.x = x
            self.y = y

    f = Foo(10, 20)
    assert str(f) == """Instance of Foo, vars = {'x': 10, 'y': 20}"""


def test_one_attribute_str_only():
    @betterrepr(newstr=replacement_str)
    class Foo():
        def __init__(self, x):
            self.x = x

    f = Foo(10)
    assert str(f) == """Replacement str, vars = {'x': 10}"""


def test_two_attributes_str_only():
    @betterrepr(newstr=replacement_str)
    class Foo():
        def __init__(self, x, y):
            self.x = x
            self.y = y

    f = Foo(10, 20)
    assert str(f) == """Replacement str, vars = {'x': 10, 'y': 20}"""


def test_one_attribute_repr_only():
    @betterrepr(newrepr=replacement_repr)
    class Foo():
        def __init__(self, x):
            self.x = x

    f = Foo(10)
    assert repr(f) == """Replacement repr, vars = {'x': 10}"""


def test_two_attributes_repr_only():
    @betterrepr(newrepr=replacement_repr)
    class Foo():
        def __init__(self, x, y):
            self.x = x
            self.y = y

    f = Foo(10, 20)
    assert repr(f) == """Replacement repr, vars = {'x': 10, 'y': 20}"""


def test_one_attribute_both():
    @betterrepr(newrepr=replacement_repr, newstr=replacement_str)
    class Foo():
        def __init__(self, x):
            self.x = x

    f = Foo(10)
    assert str(f) == """Replacement str, vars = {'x': 10}"""
    assert repr(f) == """Replacement repr, vars = {'x': 10}"""


def test_two_attributes_both():
    @betterrepr(newstr=replacement_str, newrepr=replacement_repr)
    class Foo():
        def __init__(self, x, y):
            self.x = x
            self.y = y

    f = Foo(10, 20)
    assert repr(f) == """Replacement repr, vars = {'x': 10, 'y': 20}"""
    assert str(f) == """Replacement str, vars = {'x': 10, 'y': 20}"""


test_one_attribute_default()
test_two_attributes_default()
test_one_attribute_str_only()
test_two_attributes_str_only()
test_one_attribute_repr_only()
test_two_attributes_repr_only()
test_one_attribute_both()
test_two_attributes_both()
