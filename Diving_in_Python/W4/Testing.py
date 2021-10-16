import random
import time
from abc import ABCMeta, abstractmethod
import unittest


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f'{self.name} <{self.email}>'

    def get_email_data(self):
        return {
            'name': self.name,
            'email': self.email
        }


# jane = User('Jane', 'janedoe@example.com')
# print(jane)


class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance


# a = Singleton()
# b = Singleton()

# print(a is b)


class Researcher:
    def __getattr__(self, name):
        return 'Nothing found :(\n'

    def __getattribute__(self, name):
        print(f'Looking for {name}')
        return object.__getattribute__(self, name)


# obj = Researcher()

# print(obj.attr)
# print(obj.method)
# print(obj.k)


class Ignorant:
    def __setattr__(self, name, value):
        print(f'Not gonna set {name}!')


# obj = Ignorant()
# obj.math = True


class Polite:
    def __delattr__(self, name):
        value = getattr(self, name)
        print(f'Goodbye {name}, you were {value}!')
        object.__delattr__(self, name)


# obj = Polite()

# obj.attr = 10
# del obj.attr


class Logger:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            with open(self.filename, 'w') as file_:
                file_.write('Oh Danny boy...')
            return func(*args, **kwargs)

        return wrapped


logger = Logger('log.txt')


@logger
def completely_useless_function():
    pass


# completely_useless_function()
# with open('log.txt', 'r') as f:
# print(f.read())


class NoisyInt:
    def __init__(self, value):
        self.value = value

    def __add__(self, obj_):
        noise = random.uniform(-1, 1)
        return self.value + obj_.value + noise


# a = NoisyInt(10)
# b = NoisyInt(20)
# print(a + b)


class MyVector:

    def __init__(self, size):
        self._size = size
        self._vector = [None for _ in range(10)]

    def __getitem__(self, idx):
        return self._vector[idx]

    def __setitem__(self, idx, value):
        self._vector[idx] = value

    def __str__(self):
        return self._vector.__str__()


# v = MyVector(10)

# print(v)


class SquareIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration

        result = self.current ** 2
        self.current += 1
        return result


# for num in SquareIterator(1, 4):
#  print(num)


class IndexIterable:
    def __init__(self, obj_):
        self.obj = obj_

    def __getitem__(self, index):
        return self.obj[index]


# for letter in IndexIterable('str'):
#   print(letter)


class open_file:
    def __init__(self, filename, mode):
        self.f = open(filename, mode)

    def __enter__(self):
        return self.f

    def __exit__(self, *args):
        self.f.close()


# with open_file('test.log', 'w') as f:
# f.write('Inside "open_file" context manager')

# with open_file('test.log', 'r') as f:
# print(f.read())


class suppress_exception:
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == self.exc_type:
            print('Nothing happened')
            return True


# with suppress_exception(ZeroDivisionError):
# really_big_number = 1 / 0


class timer:
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print('Elapsed:', self.current_time())

    def current_time(self):
        return time.time() - self.start


# with timer() as t:
#    time.sleep(1)
#    print('Current:', t.current_time())
#    time.sleep(1)


class Descriptor:
    def __get__(self, obj_, obj_type):
        print('get')

    def __set__(self, obj_, value):
        print('set')

    def __delete__(self, obj_):
        print('delete')


class Class:
    attr = Descriptor()


# instance = Class()
# instance.attr
# instance.attr = 10
# del instance.attr


class ImportantValue:
    def __init__(self, amount):
        self.amount = amount

    def __get__(self, obj_, obj_type):
        return self.amount

    def __set__(self, obj_, value):
        with open('log.txt', 'a') as f:
            f.write(str(value))
            self.amount = value


class Account:
    amount = ImportantValue(100)


# bobs_account = Account()
# bobs_account.amount = 150

# with open('log.txt') as f:
# print(f.read())


class User:
    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


# amy = User('Amy', 'Jones')
# print(amy.full_name)
# print(User.full_name)


class Property:
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj_, obj_type=None):
        if obj_ is None:
            return self

        return self.getter(obj_)


class Class:
    @property
    def original(self):
        return 'original'

    @Property
    def custom_sugar(self):
        return 'custom sugar'

    def custom_pure(self):
        return 'custom pure'

    custom_pure = Property(custom_pure)


# obj = Class()
# print(obj.original)
# print(obj.custom_sugar)
# print(obj.custom_pure)


class StaticMethod:
    def __init__(self, func):
        self.func = func

    def __get(self, obj_, obj_type=None):
        return self.func


class ClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj_, obj_type=None):
        if obj_type is None:
            obj_type = type(obj_)

        def new_func(*args, **kwargs):
            return self.func(obj_type, *args, **kwargs)

        return new_func


class Class:
    __slots__ = ['anakin']

    def __init__(self):
        self.anakin = 'the chosen one'


# obj = Class()
# obj.luke = 'the chosen one'


class Class:
    pass


# obj = Class()
# print(type(obj))
# print(type(Class))
# print(type(type))


def dummy_factory():
    class Class:
        pass

    return Class


# Dummy = dummy_factory()
# print(Dummy() is Dummy())

# NewClass = type('NewClass', (), {})
# print(NewClass)
# print(NewClass())

class Meta(type):
    def __new__(cls, name, parents, attrs):
        print('Creating', name)

        if 'class_id' not in attrs:
            attrs['class_id'] = name.lower()

        return super().__new__(cls, name, parents, attrs)


class Meta2(type):

    def __init__(cls, name, bases, attrs):
        print('Initializing', name)

        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            cls.registry[name.lower()] = cls

        super().__init__(name, bases, attrs)


# class Base(metaclass=Meta2):
# pass


# class A(Base):
# pass


# class B(Base):
# pass


# print(Base.registry)


class Sender(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        """Do something"""


class Child(Sender):
    def send(self):
        print('Sending')


# class TestPython(unittest.TestCase):
#     def test_float_to_int_coercion(self):
#         self.assertEqual(1, int(1.0))
#
#     def test_get_empty_dict(self):
#         self.assertIsNone({}.get('key'))
#
#     def test_trueness(self):
#         self.assertTrue(bool(10))

