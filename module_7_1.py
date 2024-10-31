from idlelib.browser import file_open
from itertools import product
from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        self.__file_name = 'products.txt'
        file_open = open(self.__file_name, 'r')
        products = file_open.read()
        file_open.close()
        return products

    def add(self, *products):

        self.file_append = open(self.__file_name, 'a')
        a = self.file_append

        for i in products:
            if i.name in self.get_products():
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                a.write(i.__str__() + '\n')

        a.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())