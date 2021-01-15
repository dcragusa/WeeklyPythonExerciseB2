
def default_newrepr(self):
    return f'Instance of {self.__class__.__name__}, vars = {vars(self)}'


def betterrepr(newstr=None, newrepr=default_newrepr):
    def wrapped(cls):
        if newstr is not None:
            cls.__str__ = newstr
        cls.__repr__ = newrepr
        return cls
    return wrapped
