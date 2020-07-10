
def magic_tuples(total, one_more_than_max):
    b = one_more_than_max - 1
    while (a := total - b) < one_more_than_max:
        yield a, b
        b -= 1
