"""Adapter Pattern"""

# Libraries
from random import random


class AdapteeShipping:
    def __init__(self, src, dst, weight):
        self.source = src
        self.destiny = dst
        self.weight = weight
        self.total = weight * 20


class TargetShipping:
    def login(self, credentials):
        pass

    def set_origin(self, src):
        self.source = src

    def set_destiny(self, dst):
        self.destiny = dst

    def calculate(self, weight):
        self.weight = weight
        total = weight * 20
        return total


class ShippingAdapater:
    def __init__(self, credentials):
        self.targetShipping = TargetShipping()
        self.targetShipping.login(credentials)

    def use(self, src, dst, weight):
        temp_obj = TargetShipping()
        temp_obj.set_origin(src)
        temp_obj.set_destiny(dst)
        return temp_obj.calculate(weight)


class Client:
    def run(self):
        src = '1234'
        dst = '2123'
        weight = 12123.2
        old_interface = AdapteeShipping
        cost = old_interface(src, dst, weight)
        print(cost.total)

        credential = {'user': 'u', 'password': 'p'}
        adapter = ShippingAdapater(credential)
        new_cost = adapter.use(src, dst, weight)
        print(new_cost)



a = Client()
a.run()
