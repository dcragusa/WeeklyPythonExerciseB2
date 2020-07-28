import os
from glob import iglob
from concurrent.futures import ThreadPoolExecutor


def count_words_file(path):
    if not os.path.isfile(path):
        return 0
    with open(path) as file:
        return sum(len(line.split()) for line in file)


def count_words_sequential(pattern):
    return sum(map(count_words_file, iglob(pattern)))


def count_words_threading(pattern):
    with ThreadPoolExecutor() as pool:
        return sum(pool.map(count_words_file, iglob(pattern)))
