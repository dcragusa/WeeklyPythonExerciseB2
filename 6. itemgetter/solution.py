
def mygetter(idxs):
    def func(iterable):
        if isinstance(idxs, tuple):
            return tuple(iterable[idx] for idx in idxs)
        else:
            return iterable[idxs]
    return func


def mygetter_lambda(idxs):
    return lambda iterable: tuple(iterable[idx] for idx in idxs) if isinstance(idxs, tuple) else iterable[idxs]
