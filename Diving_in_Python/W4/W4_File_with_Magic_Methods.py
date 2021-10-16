import os
import tempfile
import random
import string
import time


def get_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str + str(int(time.time())) + '.txt'


class IterableList:
    def __init__(self, list_):
        self.list = list_
        self.current_idx = 0
        self.end_idx = len(self.list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_idx + 1 > self.end_idx:
            raise StopIteration
        self.current_idx += 1
        return self.list[self.current_idx - 1]


class File:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        if not os.path.exists(path_to_file):
            open(path_to_file, 'w').close()

    def __str__(self):
        return self.path_to_file

    def __add__(self, other):
        new_path_to_file = os.path.join(tempfile.gettempdir(), get_random_string(10))
        with open(new_path_to_file, 'a') as new_file:
            new_file.write(open(self.path_to_file).read())
            new_file.write(open(other.path_to_file).read())
        return File(new_path_to_file)

    def __iter__(self):
        return IterableList(open(self.path_to_file).readlines())

    def read(self):
        with open(self.path_to_file, 'r') as f:
            return f.read()

    def write(self, new_str):
        with open(self.path_to_file, 'w') as f:
            f.write(new_str)

