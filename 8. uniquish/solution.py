
class Foo:
    def __init__(self, x):
        self.x = x

    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        if not isinstance(other, Foo):
            raise NotImplemented
        return self.x == other.x


class Uniquish:
    def __hash__(self):
        return hash(self.__dict__.values())

    def __eq__(self, other):
        if not isinstance(other, Uniquish):
            raise NotImplemented
        return self.__dict__ == other.__dict__
