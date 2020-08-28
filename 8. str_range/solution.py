
def str_range(start, stop, step=1):
    if step == 0:
        raise ValueError('str_range arg 3 must not be zero')
    ord_start, ord_stop = ord(start), ord(stop) + (1 if step > 0 else -1)
    yield from (chr(codepoint) for codepoint in range(ord_start, ord_stop, step))
