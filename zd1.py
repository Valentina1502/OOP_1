#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Линейное уравнение у = Ах + В. Поле first — дробное число, коэффициент A;
поле second — дробное число, коэффициент B. Реализовать метод
root() — вычисление корня линейного уравнения. Метод должен
проверять неравенство коэффициента B нулю.
'''


class Korny:

    def __init__(self):
        self.first = 0
        self.second = 0
        self.third = 0

    def root(self):
        x = (float(self.third) - float(self.second)) / float(self.first)
        print(f"   Корень  =  {x:.2f}")

    def read(self):
        self.first, self.second, self.third = \
            input("Введите коэффициенты А B и Y ").split()
        if float(self.first) != 0 and float(self.second) != 0:
            y.root()
        else:
            print("Коэффициент не может быть равен 0")


if __name__ == '__main__':
    y = Korny()
    y.read()

