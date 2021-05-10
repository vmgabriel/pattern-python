"""Pattern Singleton"""

# Libraries
from random import random


class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        self.value = random()
        Singleton.__instance = self

    def __str__(self):
        return str(self.value)


a = Singleton()
print(a)

b = Singleton.getInstance()
print(b)

c = Singleton.getInstance()
print(c)

print('a == b', a == b)
print('b == c', b == c)
