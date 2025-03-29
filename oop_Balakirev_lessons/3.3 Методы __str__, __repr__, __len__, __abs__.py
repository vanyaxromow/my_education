# Подвиг 2. Объявите класс с именем Book (книга), объекты которого создаются командой:
#
# book = Book(title, author, pages)
# где title - название книги (строка); author - автор книги (строка); pages - число страниц в книге (целое число).
#
# Также при выводе информации об объекте на экран командой:
#
# print(book)
# должна отображаться строчка в формате:
#
# "Книга: {title}; {author}; {pages}"
#
# Например:
#
# "Книга: Муму; Тургенев; 123"
#
# Прочитайте из входного потока строки с информацией по книге командой:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# (строки идут в порядке: title, author, pages). Создайте объект класса Book и выведите его строковое представление
# в консоль.


import sys


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга: {self.title}; {self.author}; {self.pages}"


lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка из входного потока (эту строчку не менять)
book = Book(*lst_in)
print(book)


# Подвиг 3. Объявите класс с именем Model, объекты которого создаются командой:
#
# model = Model()
# Объявите в этом классе метод query() для формирования записи базы данных.
# Использоваться этот метод должен следующим образом:
#
# model.query(field_1=value_1, field_2=value_2, ..., field_N=value_N)
#
# Например:
#
# model.query(id=1, fio='Sergey', old=33)
# Все эти переданные данные должны сохраняться внутри объекта model класса Model. Затем, при выполнении команды:
#
# print(model)
# В консоль должна выводиться информация об объекте в формате:
#
# "Model: field_1 = value_1, field_2 = value_2, ..., field_N = value_N"
#
# Например:
#
# "Model: id = 1, fio = Sergey, old = 33"
#
# Если метод query() не вызывался, то в консоль выводится строка:
#
# "Model"
#
# P.S. В программе нужно только объявить класс, выводить в консоль ничего не нужно.


class Model:
    def __init__(self):
        self.__params = {}

    def query(self, **kwargs):
        self.__params = kwargs

    def __str__(self):
        if self.__params:
            return f"Model: {', '.join(list(map(lambda x: f'{x} = {self.__params[x]}', self.__params)))}"
        return 'Model'


model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)


# Подвиг 4. Объявите класс WordString, объекты которого создаются командами:
#
# w1 = WordString()
# w2 = WordString(string)
# где string - передаваемая строка. Например:
#
# words = WordString("Курс по Python ООП")
# Реализовать следующий функционал для объектов этого класса:
#
# len(words) - должно возвращаться число слов в переданной строке (слова разделяются одним или несколькими пробелами);
# words(indx) - должно возвращаться слово по его индексу (indx - порядковый номер слова в строке, начиная с 0).
#
# Также в классе WordString реализовать объект-свойство (property):
#
# string - для передачи и считывания строки.
#
# Пример пользования классом WordString (эти строчки в программе писать не нужно):
#
# words = WordString()
# words.string = "Курс по Python ООП"
# n = len(words)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(f"Число слов: {n}; первое слово: {first}")
# P.S. В программе нужно только объявить класс, выводить в консоль ничего не нужно.


class WordString:
    def __init__(self, string=None):
        self.strings = string

    def __len__(self):
        return len(self.strings.split())

    def words(self, indx):
        return self.strings.split()[indx]

    @property
    def string(self):
        return self.strings

    @string.setter
    def string(self, value):
        self.strings = value

    def __call__(self, indx, *args, **kwargs):
        return self.words(indx)


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")


# Подвиг 5. Объявите класс LinkedList (связный список) для работы со следующей структурой данных:
#
#
#
# Здесь создается список из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:
#
# obj = ObjList(data)
# где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться
# следующие локальные атрибуты:
#
# __data - ссылка на строку с данными;
# __prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
# __next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).
#
# В свою очередь, объекты класса LinkedList должны создаваться командой:
#
# linked_lst = LinkedList()
# и содержать локальные атрибуты:
#
# head - ссылка на первый объект связного списка (если список пуст, то head = None);
# tail - ссылка на последний объект связного списка (если список пуст, то tail = None).
#
# А сам класс содержать следующие методы:
#
# add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
# remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу);
# индекс отсчитывается с нуля.
#
# Также с объектами класса LinkedList должны поддерживаться следующие операции:
#
# len(linked_lst) - возвращает число объектов в связном списке;
# linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под
# индексом indx (в связном списке).
#
# Пример использования классов (эти строчки в программе писать не нужно):
#
# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)  # n = 3
# s = linked_lst(1) # s = Balakirev
# P.S. На экран в программе ничего выводить не нужно.


class Descriptor:
    def __set_name__(self, owner, name):
        self.name = f"_{owner.__name__}__{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class ObjList:
    data = Descriptor()
    prev = Descriptor()
    next = Descriptor()

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail:
            ptr = obj
            self.tail.next = ptr
            ptr.prev = self.tail
            self.tail = ptr

        else:
            self.head = self.tail = obj

    def remove_obj(self, indx):
        ptr = self.head
        number = 0
        while ptr:
            if indx != number:
                number += 1
                ptr = ptr.next
            elif indx == number:
                if ptr is self.head:
                    if not self.head.next:
                        self.head = None
                        self.tail = None
                        break
                    ptr = self.head.next
                    ptr.prev = None
                    self.head = ptr
                    break

                elif ptr is self.tail:
                    ptr = self.tail.prev
                    ptr.next = None
                    self.tail = ptr
                    break

            else:
                left = ptr.prev
                right = ptr.next
                left.next = right
                right.prev = left
                break

    def __len__(self):
        ptr = self.head
        amount = 1
        while ptr.next:
            ptr = ptr.next
            amount += 1

        return amount if ptr else 0

    def __call__(self, indx, *args, **kwargs):
        ptr = self.head
        number = 0
        while ptr:
            if number == indx:
                return ptr.data
            ptr = ptr.next
            number += 1


ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(
    ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"
#
n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"


# Подвиг 6. Объявите класс с именем Complex для представления и работы с комплексными числами.
# Объекты этого класса должны создаваться командой:
#
# cm = Complex(real, img)
# где real - действительная часть комплексного числа (целое или вещественное значение); img - мнимая часть
# комплексного числа (целое или вещественное значение).
#
# Объявите в этом классе следующие объекты-свойства (property):
#
# real - для записи и считывания действительного значения;
# img - для записи и считывания мнимого значения.
#
# При записи новых значений необходимо проверять тип передаваемых данных. Если тип не соответствует целому или
# вещественному числу, то генерировать исключение командой:
#
# raise ValueError("Неверный тип данных.")
# Также с объектами класса Complex должна поддерживаться функция:
#
# res = abs(cm)
# возвращающая модуль комплексного числа (вычисляется по формуле: sqrt(real*real + img*img) - корень квадратный
# от суммы квадратов действительной и мнимой частей комплексного числа).
#
# Создайте объект cmp класса Complex для комплексного числа с real = 7 и img = 8. Затем, через объекты-свойства
# real и img измените эти значения на real = 3 и img = 4. Вычислите модуль полученного комплексного числа
# (сохраните результат в переменной c_abs).
#
# P.S. На экран ничего выводить не нужно.


from math import sqrt


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    @classmethod
    def verify_value(cls, value):
        if type(value) not in (int, float):
            raise ValueError("Неверный тип данных.")

    @property
    def real(self):
        return self.__real

    @real.setter
    def real(self, value):
        self.verify_value(value)
        self.__real = value

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.verify_value(value)
        self.__img = value

    def __abs__(self):
        return abs(sqrt(self.real*self.real + self.img*self.img))


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(c_abs)


# Подвиг 7. Объявите класс с именем RadiusVector для описания и работы с n-мерным вектором (у которого n координат).
# Объекты этого класса должны создаваться командами:
#
# # создание 5-мерного радиус-вектора с нулевыми значениями координат (аргумент - целое число больше 1)
# vector = RadiusVector(5)  # координаты: 0, 0, 0, 0, 0
#
# # создание 4-мерного радиус-вектора с координатами: 1, -5, 3.4, 10 (координаты - любые целые или вещественные числа)
# vector = RadiusVector(1, -5, 3.4, 10)
# То есть, при передаче одного значения, оно интерпретируется, как размерность нулевого радиус-вектора.
# Если же передается более одного числового аргумента, то они интерпретируются, как координаты радиус-вектора.
#
# Класс RadiusVector должен содержать методы:
#
# set_coords(coord_1, coord_2, ..., coord_N) - для изменения координат радиус-вектора;
# get_coords() - для получения текущих координат радиус-вектора (в виде кортежа).
#
# Также с объектами класса RadiusVector должны поддерживаться следующие функции:
#
# len(vector) - возвращает число координат радиус-вектора (его размерность);
# abs(vector) - возвращает длину радиус-вектора (вычисляется как: sqrt(coord_1*coord_1 + coord_2*coord_2 + ...
#                                                                      + coord_N*coord_N) - корень квадратный
# из суммы квадратов координат).
#
# Пример использования класса RadiusVector (эти строчки в программе писать не нужно):
#
# vector3D = RadiusVector(3)
# vector3D.set_coords(3, -5.6, 8)
# a, b, c = vector3D.get_coords()
# vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
# vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
# res_len = len(vector3D) # res_len = 3
# res_abs = abs(vector3D)
# P.S. На экран ничего выводить не нужно, только объявить класс RadiusVector.


class RadiusVector:
    def __init__(self, *args):
        self.coords = None
        if len(args) == 1 and type(args[0]) is int and args[0] > 1:
            self.coords = [0 for _ in range(args[0])]
        elif len(args) > 1:
            self.coords = [x for x in args]

    def set_coords(self, *args):
        s = min(len(self.coords), len(args))
        for i in range(s):
            self.coords[i] = args[i]

        return self.coords

    def get_coords(self):
        return tuple(self.coords)

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        res = sum([x*x for x in self.coords])**0.5
        return res


vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
print(vector3D.get_coords())


# Подвиг 8. Объявите класс DeltaClock для вычисления разницы времен. Объекты этого класса должны создаваться
# командой:
#
# dt = DeltaClock(clock1, clock2)
# где clock1, clock2 - объекты другого класса Clock для хранения текущего времени. Эти объекты должны создаваться
# командой:
#
# clock = Clock(hours, minutes, seconds)
# где hours, minutes, seconds - часы, минуты, секунды (целые неотрицательные числа).
#
# В классе Clock также должен быть (по крайней мере) один метод (возможны и другие):
#
# get_time() - возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds).
#
# После создания объекта dt класса DeltaClock, с ним должны выполняться команды:
#
# str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
# len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
# print(dt)   # отображает строку разницы времен clock1 - clock2 в формате: часы: минуты: секунды
# Если разность получается отрицательной, то разницу времен считать нулевой.
#
# Пример использования классов (эти строчки в программе писать не нужно):
#
# dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
# print(dt) # 01: 30: 00
# len_dt = len(dt) # 5400
# Обратите внимание, добавляется незначащий ноль, если число меньше 10.
#
# P.S. На экран ничего выводить не нужно, только объявить классы.


class DeltaClock:
    def __init__(self, obj_1, obj_2):
        self.obj_1 = obj_1
        self.obj_2 = obj_2

    def __str__(self):
        diff = self.__len__()
        h = diff // 3600
        m = diff % 3600 // 60
        s = diff % 3600 % 60
        return f'{h:02}: {m:02}: {s:02}'

    def __len__(self):
        res = self.obj_1.get_time() - self.obj_2.get_time()
        return res if res > 0 else 0


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400
print(len_dt)


# Подвиг 9. Объявите класс Recipe для представления рецептов. Отдельные ингредиенты рецепта должны определяться
# классом Ingredient. Объекты этих классов должны создаваться командами:
#
# ing = Ingredient(name, volume, measure)
# recipe = Recipe()
# recipe = Recipe(ing_1, ing_2,..., ing_N)
# где ing_1, ing_2,..., ing_N - объекты класса Ingredient.
#
# В каждом объекте класса Ingredient должны создаваться локальные атрибуты:
#
# name - название ингредиента (строка);
# volume - объем ингредиента в рецепте (вещественное число);
# measure - единица измерения объема ингредиента (строка), например, литр, чайная ложка, грамм, штук и т.д.;
#
# С объектами класса Ingredient должна работать функция:
#
# str(ing)  # название: объем, ед. изм.
# и возвращать строковое представление объекта в формате:
#
# "название: объем, ед. изм."
#
# Например:
#
# ing = Ingredient("Соль", 1, "столовая ложка")
# s = str(ing) # Соль: 1, столовая ложка
# Класс Recipe должен иметь следующие методы:
#
# add_ingredient(ing) - добавление нового ингредиента ing (объект класса Ingredient) в рецепт (в конец);
# remove_ingredient(ing) - удаление ингредиента по объекту ing (объект класса Ingredient) из рецепта;
# get_ingredients() - получение кортежа из объектов класса Ingredient текущего рецепта.
#
# Также с объектами класса Recipe должна поддерживаться функция:
#
# len(recipe) - возвращает число ингредиентов в рецепте.
#
# Пример использования классов (эти строчки в программе писать не нужно):
#
# recipe = Recipe()
# recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
# recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
# recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
# ings = recipe.get_ingredients()
# n = len(recipe) # n = 3
# P.S. На экран ничего выводить не нужно, только объявить классы.


class Recipe:
    def __init__(self, *args):
        self.recipes = list(args)

    def add_ingredient(self, ing):
        self.recipes.append(ing)

    def remove_ingredient(self, ing):
        if ing in self.recipes:
            self.recipes.remove(ing)

    def get_ingredients(self):
        return tuple(self.recipes)

    def __len__(self):
        return len(self.recipes)


class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3


# Подвиг 10 (на повторение). Объявите класс PolyLine (полилиния) для представления линии из последовательности
# прямолинейных сегментов. Объекты этого класса должны создаваться командой:
#
# poly = PolyLine(start_coord, coord_2, coord_3, ..., coord_N)
# Здесь start_coord - координата начала полилинии (кортеж из двух чисел x, y); coord_2, coord_3, ... - последующие
# координаты точек на плоскости (представленные кортежами), соединенных прямыми линиями.
#
# Например:
#
# poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
#
#
# В классе PolyLine должны быть объявлены следующие методы:
#
# add_coord(x, y) - добавление новой координаты (в конец);
# remove_coord(indx) - удаление координаты по индексу (порядковому номеру, начинается с нуля);
# get_coords() - получение списка координат (в виде списка из кортежей).
#
# P.S. На экран ничего выводить не нужно, только объявить класс.


class PolyLine:
    def __init__(self, start_coord, *args):
        self.coords = [start_coord, *args]

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        del self.coords[indx]

    def get_coords(self):
        return self.coords


poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
print(poly.get_coords())
