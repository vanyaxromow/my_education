# Подвиг 4. Объявите в программе класс с именем Rect (прямоугольник), объекты которого создаются командой:
#
# rect = Rect(x, y, width, height)
# где x, y - координата верхнего левого угла (числа: целые или вещественные); width, height - ширина и высота
# прямоугольника (числа: целые или вещественные).
#
# В этом классе определите магический метод, чтобы хэши объектов класса Rect с равными width, height были равны.
# Например:
#
# r1 = Rect(10, 5, 100, 50)
# r2 = Rect(-10, 4, 100, 50)
#
# h1, h2 = hash(r1), hash(r2)   # h1 == h2
# P.S. На экран ничего выводить не нужно, только объявить класс.


class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __eq__(self, other):
        return self.width, self.height == other.width, other.height

    def __hash__(self):
        return hash((self.width, self.height))


r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)   # h1 == h2
print(h1 == h2)


# Подвиг 6. Объявите класс с именем ShopItem (товар), объекты которого создаются командой:
#
# item = ShopItem(name, weight, price)
# где name - название товара (строка); weight - вес товара (число: целое или вещественное); price - цена товара
# (число: целое или вещественное).
#
# Определите в этом классе магические методы:
#
# __hash__() - чтобы товары с одинаковым названием (без учета регистра), весом и ценой имели бы равные хэши;
# __eq__() - чтобы объекты с одинаковыми хэшами были равны.
#
# Затем, из входного потока прочитайте строки командой:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Строки имеют следующий формат:
#
# название товара 1: вес_1 цена_1
# ...
# название товара N: вес_N цена_N
#
# Например:
#
# Системный блок: 1500 75890.56
# Монитор Samsung: 2000 34000
# Клавиатура: 200.44 545
# Монитор Samsung: 2000 34000
#
# Как видите, товары в этом списке могут совпадать.
#
# Необходимо для всех этих строчек сформировать соответствующие объекты класса ShopItem и добавить в словарь с
# именем shop_items. Ключами словаря должны выступать сами объекты, а значениями - список в формате:
#
# [item, total]
#
# где item - объект класса ShopItem; total - общее количество одинаковых объектов (с одинаковыми хэшами). Подумайте,
# как эффективно программно наполнять такой словарь, проходя по списку lst_in один раз.
#
# P.S. На экран ничего выводить не нужно, только объявить класс и сформировать словарь.
#
# Sample Input:
#
# Системный блок: 1500 75890.56
# Монитор Samsung: 2000 34000
# Клавиатура: 200.44 545
# Монитор Samsung: 2000 34000
# Sample Output:


import sys


class ShopItem:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f'{self.name} - {self.weight} - {self.price}'

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return self.name.lower(), self.weight, self.price == other.name.lower(), other.weight, other.price


# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять!
shop_items = {}
lst = []

for i in lst_in:
    name, weight, price = i.rsplit(maxsplit=2)
    obj = ShopItem(name[:], weight, price)
    shop_items.setdefault(obj, [obj, 0])[1] += 1
print(shop_items)


# Подвиг 7. Объявите класс с именем DataBase (база данных - БД), объекты которого создаются командой:
#
# db = DataBase(path)
# где path - путь к файлу с данными БД (строка).
#
# Также в классе DataBase нужно объявить следующие методы:
#
# write(self, record) - для добавления новой записи в БД, представленной объектом record;
# read(self, pk) - чтение записи из БД (возвращает объект Record) по ее уникальному идентификатору pk
# (уникальное целое положительное число); запись ищется в значениях словаря (см. ниже)
#
# Каждая запись БД должна описываться классом Record, а объекты этого класса создаваться командой:
#
# record = Record(fio, descr, old)
# где fio - ФИО некоторого человека (строка); descr - характеристика человека (строка); old - возраст человека
# (целое число).
#
# В каждом объекте класса Record должны формироваться следующие локальные атрибуты:
#
# pk - уникальный идентификатор записи (число: целое, положительное); формируется автоматически при создании
# каждого нового объекта;
# fio - ФИО человека (строка);
# descr - характеристика человека (строка);
# old - возраст человека (целое число).
#
# Реализовать для объектов класса Record вычисление хэша по атрибутам: fio и old (без учета регистра).
# Если они одинаковы для разных записей, то и хэши должны получаться равными. Также для объектов класса Record
# с одинаковыми хэшами оператор == должен выдавать значение True, а с разными хэшами - False.
#
# Хранить записи в БД следует в виде словаря dict_db (атрибут объекта db класса DataBase), ключами которого
# являются объекты класса Record, а значениями список из объектов с равными хэшами:
#
# dict_db[rec1] = [rec1, rec2, ..., recN]
#
# где rec1, rec2, ..., recN - объекты класса Record с одинаковыми хэшами.
#
# Для наполнения БД прочитайте строки из входного потока с помощью команды:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# где каждая строка представлена в формате:
#
# "ФИО; характеристика; возраст"
#
# Например:
#
# Балакирев С.М.; программист; 33
# Кузнецов А.В.; разведчик-нелегал; 35
# Суворов А.В.; полководец; 42
# Иванов И.И.; фигурант всех подобных списков; 26
# Балакирев С.М.; преподаватель; 37
#
# Каждая строка должна быть представлена объектом класса Record и записана в БД db (в словарь db.dict_db).
#
# P.S. На экран ничего выводить не нужно.
#
# Sample Input:
#
# Балакирев С.М.; программист; 33
# Кузнецов Н.И.; разведчик-нелегал; 35
# Суворов А.В.; полководец; 42
# Иванов И.И.; фигурант всех подобных списков; 26
# Балакирев С.М.; преподаватель; 33
# Sample Output:


import sys


class DataBase:
    list_db = []

    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, [])
        self.dict_db[record].append(record)

    def read(self, pk):
        for i in self.dict_db.values():
            for j in i:
                if j.pk == pk:
                    return j


class Record:
    id = 1

    def __init__(self, fio, descr, old):
        self.fio = str(fio)
        self.descr = str(descr)
        self.old = int(old)
        self.pk = Record.id
        Record.id += 1

    def __repr__(self):
        return f'{self.fio} - {self.descr} - {self.old}'

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self.fio), hash(self.old) == hash(other.fio), hash(other.old)


# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in не менять!

# здесь продолжайте программу (используйте список строк lst_in)
db = DataBase('path')
for i in lst_in:
    db.write(Record(*i.split(';')))


# Подвиг 8. Из входного потока необходимо прочитать список строк командой:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Каждая строка содержит информацию об учебном пособии в формате:
#
# "Название; автор; год издания"
#
# Например:
#
# Python; Балакирев С.М.; 2020
# Python ООП; Балакирев С.М.; 2021
# Python ООП; Балакирев С.М.; 2022
# Python; Балакирев С.М.; 2021
#
# Необходимо каждую из этих строк представить объектом класса BookStudy, которые создаются командой:
#
# bs = BookStudy(name, author, year)
# где name - название пособия (строка); author - автор пособия (строка); year - год издания (целое число).
# Такие же публичные локальные атрибуты должны быть в объектах класса BookStudy.
#
# Для каждого объекта реализовать вычисление хэша по двум атрибутам: name и author (без учета регистра).
#
# Сформировать список lst_bs из объектов класса BookStudy на основе прочитанных строк (списка lst_in).
# После этого определить число книг с уникальными хэшами. Это число сохранить через переменную unique_books
# (целое число).
#
# P.S. На экран ничего выводить не нужно.
#
# Sample Input:
#
# Python; Балакирев С.М.; 2020
# Python ООП; Балакирев С.М.; 2021
# Python ООП; Балакирев С.М.; 2022
# Python; Балакирев С.М.; 2021
# Sample Output:


import sys


class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)


# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in не менять!

lst_bs = [BookStudy(*x.split(';')) for x in lst_in]
unique_books = sum(hash(x) != hash(lst_bs[0]) for x in lst_bs)
print(unique_books)


# Подвиг 9 (релакс). Объявите класс с именем Dimensions, объекты которого создаются командой:
#
# d = Dimensions(a, b, c)
# где a, b, c - положительные числа (целые или вещественные), описывающие габариты некоторого тела: высота,
# ширина и глубина.
#
# Каждый объект класса Dimensions должен иметь аналогичные публичные атрибуты a, b, c (с соответствующими числовыми
# значениями). Также для каждого объекта должен вычисляться хэш на основе всех трех габаритов: a, b, c.
#
# С помощью функции input() прочитайте из входного потока строку, записанную в формате:
#
# "a1 b1 c1; a2 b2 c2; ... ;aN bN cN"
#
# Например:
#
# "1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"
#
# Если какой-либо габарит оказывается отрицательным значением или равен нулю, то при создании объектов должна
# генерироваться ошибка командой:
#
# raise ValueError("габаритные размеры должны быть положительными числами")
# Сформируйте на основе прочитанной строки список lst_dims из объектов класса Dimensions. После этого отсортируйте
# этот список по возрастанию (неубыванию) хэшей этих объектов так, чтобы объекты с равными хэшами стояли друг за
# другом.
#
# P.S. На экран ничего выводить не нужно.
#
# Sample Input:
#
# 1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5
# Sample Output:


# s_inp = input()  # эту строку (переменную s_inp) в программе не менять
#
#
class Dimensions:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.__valid_attr(self.a, self.b, self.c)

    def __valid_attr(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")

    def __hash__(self):
        return hash((self.a, self.b, self.c))


lst = [list(map(lambda i: float(i), x)) for row in s_inp.split('; ') for x in [row.split()]]
lst_dims = [Dimensions(*x) for x in lst]
lst_dims.sort(key=hash)
print(lst_dims)


# Подвиг 10 (на повторение). Объявите класс с именем Triangle, объекты которого создаются командой:
#
# tr = Triangle(a, b, c)
# где a, b, c - длины сторон треугольника (числа: целые или вещественные). В классе Triangle объявите следующие
# дескрипторы данных:
#
# a, b, c - для записи и считывания длин сторон треугольника.
#
# При записи нового значения нужно проверять, что присваивается положительное число (целое или вещественное).
# Иначе, генерируется исключение командой:
#
# raise ValueError("длины сторон треугольника должны быть положительными числами")
# Также нужно проверять, что все три стороны a, b, c могут образовывать стороны треугольника. То есть, должны
# выполняться условия:
#
# a < b+c; b < a+c; c < a+b
#
# Иначе генерируется исключение командой:
#
# raise ValueError("с указанными длинами нельзя образовать треугольник")
# Наконец, с объектами класса Triangle должны выполняться функции:
#
# len(tr) - возвращает периметр треугольника, приведенный к целому значению с помощью функции int();
# tr() - возвращает площадь треугольника (можно вычислить по формуле Герона: s = sqrt(p * (p-a) * (p-b) * (p-c)),
# где p - полупериметр треугольника).
#
# P.S. На экран ничего выводить не нужно, только объявить класс Triangle.


class Integer:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if type(value) not in (int, float) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance, self.name, value)


class Triangle:
    a = Integer()
    b = Integer()
    c = Integer()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def __is_triangle(a, b, c):
        if a and b and c:
            return a < b + c and b < a+c and c < a+c
        return True

    def __setattr__(self, key, value):
        if (key == 'a' and not self.__is_triangle(value, self.b, self.c)) or \
                (key == 'b' and not self.__is_triangle(self.a, value, self.c)) or \
                (key == 'c' and not self.__is_triangle(self.a, self.b, value)):
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        super().__setattr__(key, value)

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        p = (self.a + self.b + self.c) / 2
        s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return s




