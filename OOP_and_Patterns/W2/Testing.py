# Abstractions with abc
# from abc import ABC, abstractmethod
#
#
# class A:
#     @abstractmethod
#     def do_something(self):
#         print("Hi")
#
#
# a = A()
# a.do_something()
#
#
# class A1(ABC):
#     @abstractmethod
#     def do_something(self):
#         print("Hi")
#
#
# class B(A1):
#     def do_something_else(self):
#         print("Something")
#
#     def do_something(self):
#         print("Hi2!")
#
#
# b = B()
# b.do_something()
from abc import ABC, abstractmethod


class A(ABC):
    def __init__(self):
        self.var1 = 5
        self.var2 = 7

    @abstractmethod
    def do_something(self):
        print(self.var1 + self.var2)


class B(A):
    def __init__(self):
        self.var1 = 2


obj = B()
obj.do_something()
