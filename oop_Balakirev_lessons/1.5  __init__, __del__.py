# Подвиг 2. Объявите класс Money так, чтобы объекты этого класса можно было создавать следующим
# образом:
#
# my_money = Money(100)
# your_money = Money(1000)
# Здесь при создании объектов указывается количество денег, которое должно сохраняться в локальном свойстве
# (атрибуте) money каждого экземпляра класса.
#
# P.S. На экран в программе ничего выводить не нужно.


class Money:
    def __init__(self, money):
        self.money = money


my_money = Money(100)
your_money = Money(1000)


# Подвиг 3. Объявите класс Point так, чтобы объекты этого класса можно было создавать командами:
#
# p1 = Point(10, 20)
# p2 = Point(12, 5, 'red')
# Здесь первые два значения - это координаты точки на плоскости (локальные свойства x, y), а третий
# необязательный аргумент - цвет точки (локальное свойство color). Если цвет не указывается, то он по
# умолчанию принимает значение black.
#
# Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ... то есть, с увеличением на два
# для каждой новой точки. Каждый объект следует поместить в список points (по порядку). Для второго объекта
# в списке points укажите цвет 'yellow'.
#
# P.S. На экран в программе ничего выводить не нужно.


class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = [Point(x*2+1, x*2+1) for x in range(1000)]
points[1].color = 'yellow'

points = []
x = 1
y = 1
for i in range(1, 1001):
    if i == 2:
        pi = Point(x, y, 'yellow')
    else:
        pi = Point(x, y)
    points.append(pi)
    x += 2
    y += 2


# Подвиг 4. Объявите три класса геометрических фигур: Line, Rect, Ellipse. Должна быть возможность создавать
# объекты каждого класса следующими командами:
#
# g1 = Line(a, b, c, d)
# g2 = Rect(a, b, c, d)
# g3 = Ellipse(a, b, c, d)
# Здесь в качестве аргументов a, b, c, d передаются координаты верхнего правого и нижнего левого углов
# (произвольные числа). В каждом объекте координаты должны сохраняться в локальных свойствах sp (верхний
# правый угол) и ep (нижний левый) в виде кортежей (a, b) и (c, d) соответственно.
#
# Сформируйте 217 объектов этих классов: для каждого текущего объекта класс выбирается случайно (или Line,
# или Rect, или Ellipse). Координаты также генерируются случайным образом (числовые значения). Все объекты
# сохраните в списке elements.
#
# В списке elements обнулите координаты объектов только для класса Line.
#
# P.S. На экран в программе ничего выводить не нужно.

import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


lst = [Rect, Line, Ellipse]
elements = [random.choice(lst)(*random.sample([x for x in range(1, 100)], 4)) for x in range(217)]

for i in elements:
    if isinstance(i, Line):
        i.sp = 0, 0
        i.ep = 0, 0


# Подвиг 5. Объявите класс TriangleChecker, объекты которого можно было бы создавать командой:
#
# tr = TriangleChecker(a, b, c)
# Здесь a, b, c - длины сторон треугольника.
#
# В классе TriangleChecker необходимо объявить метод is_triangle(), который бы возвращал следующие коды:
#
# 1 - если хотя бы одна сторона не число (не float или int) или хотя бы одно число меньше или равно нулю;
# 2 - указанные числа a, b, c не могут являться длинами сторон треугольника;
# 3 - стороны a, b, c образуют треугольник.
#
# Проверку параметров a, b, c проводить именно в таком порядке.
#
# Прочитайте из входного потока строку, содержащую три числа, разделенных пробелами, командой:
#
# a, b, c = map(int, input().split())
# Затем, создайте объект tr класса TriangleChecker и передайте ему прочитанные значения a, b, c. Вызовите метод
# is_triangle() из объекта tr и выведите результат на экран (код, который она вернет).


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        lst = [self.a, self.b, self.c]
        if any(map(lambda x: type(x) is not float and type(x) is not int or x <= 0, lst)):
            return 1
        lst.sort(reverse=True)
        if lst[0] > lst[1] + lst[2]:
            return 2

        return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())


# Подвиг 6. Объявите класс Graph, объекты которого можно было бы создавать с помощью команды:
#
# gr_1 = Graph(data)
# где data - список из числовых данных (данные для графика). При создании каждого экземпляра класса
# должны формироваться следующие локальные свойства:
#
# data - ссылка на список из числовых данных (у каждого объекта должен быть свой список с данными,
# нужно создавать копию переданного списка);
# is_show - булево значение (True/False) для показа (True) и сокрытия (False) данных графика
# (по умолчанию True);
#
# В этом классе объявите следующие методы:
#
# set_data(self, data) - для передачи нового списка данных в текущий график;
# show_table(self) - для отображения данных в виде строки из списка чисел (числа следуют через пробел);
# show_graph(self) - для отображения данных в виде графика (метод выводит в консоль сообщение:
# "Графическое отображение данных: <строка из чисел следующих через пробел>");
# show_bar(self) - для отображения данных в виде столбчатой диаграммы (метод выводит в консоль сообщение:
# "Столбчатая диаграмма: <строка из чисел следующих через пробел>");
# set_show(self, fl_show) - метод для изменения локального свойства is_show на переданное значение fl_show.
#
# Если локальное свойство is_show равно False, то методы show_table(), show_graph() и show_bar()
# должны выводить сообщение:
#
# "Отображение данных закрыто"
#
# Прочитайте из входного потока числовые данные с помощью команды:
#
# data_graph = list(map(int, input().split()))
# Создайте объект gr класса Graph с набором прочитанных данных, вызовите метод show_bar(), затем метод
# set_show() со значением fl_show = False и вызовите метод show_table(). На экране должны отобразиться
# две соответствующие строки.
#
# Sample Input:
#
# 8 11 10 -32 0 7 18
# Sample Output:
#
# Столбчатая диаграмма: 8 11 10 -32 0 7 18
# Отображение данных закрыто


class Graph:
    def __init__(self, data, is_show=True):
        self.data = data[:]
        self.is_show = is_show

    def set_data(self, data):
        self.data = data[:]

    def get_data(self):
        print("Отображение данных закрыто")

    def show_table(self):
        if self.is_show is False:
            self.get_data()
        else:
            print(*self.data)

    def show_graph(self):
        if self.is_show is False:
            self.get_data()
        else:
            print(f"Графическое отображение данных:", *self.data)

    def show_bar(self):
        if self.is_show is False:
            self.get_data()
        else:
            print(f"Столбчатая диаграмма:", *self.data)

    def set_show(self, fl_show):
        self.is_show = fl_show


# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(fl_show=False)
gr.show_table()


# Подвиг 7. Объявите в программе следующие несколько классов:
#
# CPU - класс для описания процессоров;
# Memory - класс для описания памяти;
# MotherBoard - класс для описания материнских плат.
#
# Обеспечить возможность создания объектов каждого класса командами:
#
# cpu = CPU(наименование, тактовая частота)
# mem = Memory(наименование, размер памяти)
# mb = MotherBoard(наименование, процессор, память1, память2, ..., памятьN)
# Обратите внимание при создании объекта класса MotherBoard можно передавать несколько объектов класса
# Memory, максимум N - по числу слотов памяти на материнской плате (N = 4).
#
# Объекты классов должны иметь следующие локальные свойства:
#
# для класса CPU: name - наименование; fr - тактовая частота;
# для класса Memory: name - наименование; volume - объем памяти;
# для класса MotherBoard: name - наименование; cpu - ссылка на объект класса CPU;
# total_mem_slots = 4 - общее число слотов памяти (атрибут прописывается с этим значением и не меняется);
# mem_slots - список из объектов класса Memory (максимум total_mem_slots = 4 штук по максимальному
# числу слотов памяти).
#
# Класс MotherBoard должен иметь метод get_config(self) для возвращения текущей конфигурации компонентов
# на материнской плате в виде следующего списка из четырех строк:
#
# ['Материнская плата: <наименование>',
# 'Центральный процессор: <наименование>, <тактовая частота>',
# 'Слотов памяти: <общее число слотов памяти>',
# 'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']
#
# Создайте объект mb класса MotherBoard с одним CPU (объект класса CPU) и двумя слотами памяти (объекты
# класса Memory).
#
# P.S. Отображать на экране ничего не нужно, только создать объект по указанным требованиям.


class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *args):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = args

    def get_config(self):
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                f'Память: {'; '.join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots))}']


mb = MotherBoard("ASUS ROG", CPU("Intel Core i7", "3.6GHz"), Memory("Corsair", "16GB"), Memory("Kingston", "8GB"))
print(mb.get_config())


# Подвиг 8. Объявите в программе класс Cart (корзина), объекты которого создаются командой:
#
# cart = Cart()
# Каждый объект класса Cart должен иметь локальное свойство goods - список объектов для покупки
# (объекты классов Table, TV, Notebook и Cup). Изначально этот список должен быть пустым.
#
# В классе Cart объявить методы:
#
# add(self, gd) - добавление в корзину товара, представленного объектом gd;
# remove(self, indx) - удаление из корзины товара по индексу indx;
# get_list(self) - получение из корзины товаров в виде списка из строк:
#
# ['<наименовние_1>: <цена_1>',
# '<наименовние_2>: <цена_2>',
# ...
# '<наименовние_N>: <цена_N>']
#
# Объявите в программе следующие классы для описания товаров:
#
# Table - столы;
# TV - телевизоры;
# Notebook - ноутбуки;
# Cup - кружки.
#
# Объекты этих классов должны создаваться командой:
#
# gd = ИмяКласса(name, price)
# Каждый объект классов товаров должен содержать локальные свойства:
#
# name - наименование;
# price - цена.
#
# Создайте в программе объект cart класса Cart. Добавьте в него два телевизора (TV), один стол (Table),
# два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами.
#
# P.S. Отображать на экране ничего не нужно, только создать объекты по указанным требованиям.


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, *gd):
        self.goods += gd

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        lst = [f'{x.name}: {x.price}' for x in self.goods]
        return lst


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV(Table):
    pass


class Notebook(Table):
    pass


class Cup(Table):
    pass


cart = Cart()
cart.add(TV('LG', 1000), TV('Samsung', 10000), Table('Ikea', 500)
         , Notebook('Apple', 30000), Notebook('Samsung', 10000),
         Cup('Smile', 10))

print(cart.goods)
print(cart.get_list())


# Подвиг 9. Вам необходимо реализовать односвязный список (не список языка Python, объекты в списке не
# хранить, а формировать связанную структуру, показанную на рисунке) из объектов класса ListObject:
#
#
#
# Для этого объявите в программе класс ListObject, объекты которого создаются командой:
#
# obj = ListObject(data)
# Каждый объект класса ListObject должен содержать локальные свойства:
#
# next_obj - ссылка на следующий присоединенный объект (если следующего объекта нет, то next_obj = None);
# data - данные объекта в виде строки.
#
# В самом классе ListObject должен быть объявлен метод:
#
# link(self, obj) - для присоединения объекта obj такого же класса к текущему объекту self (то есть,
# атрибут next_obj объекта self должен ссылаться на obj).
#
# Прочитайте список строк из входного потока командой:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# Затем сформируйте односвязный список, в объектах которых (в атрибуте data) хранятся строки из списка
# lst_in (первая строка в первом объекте, вторая - во втором и  т.д.). На первый добавленный объект
# класса ListObject должна ссылаться переменная head_obj.
#
# P.S. В программе что-либо выводить на экран не нужно.
#
# Sample Input:
#
# 1. Первые шаги в ООП
# 1.1 Как правильно проходить этот курс
# 1.2 Концепция ООП простыми словами
# 1.3 Классы и объекты. Атрибуты классов и объектов
# 1.4 Методы классов. Параметр self
# 1.5 Инициализатор init и финализатор del
# 1.6 Магический метод new. Пример паттерна Singleton
# 1.7 Методы класса (classmethod) и статические методы (staticmethod)
# Sample Output:


import sys


class ListObject:
    def __init__(self, data, next_obj=None):
        self.data = data
        self.next_obj = next_obj

    def link(self, obj):
        self.next_obj = obj


lst_in = list(map(str.strip, sys.stdin.readlines()))

head_obj = ListObject(lst_in[0])
tail_obj = ListObject(lst_in[1])
head_obj.link(tail_obj)

for i in range(2, len(lst_in)):
    node = ListObject(lst_in[i])
    tail_obj.link(node)
    tail_obj = node

print(tail_obj.data)


# Большой подвиг 10. Объявите два класса:
#
# Cell - для представления клетки игрового поля;
# GamePole - для управления игровым полем, размером N x N клеток.
#
# С помощью класса Cell предполагается создавать отдельные клетки командой:
#
# c1 = Cell(around_mines, mine)
# Здесь around_mines - число мин вокруг данной клетки поля; mine - булева величина (True/False),
# означающая наличие мины в текущей клетке. При этом, в каждом объекте класса Cell должны создаваться
# локальные свойства:
#
# around_mines - число мин вокруг клетки (начальное значение 0);
# mine - наличие/отсутствие мины в текущей клетке (True/False);
# fl_open - открыта/закрыта клетка - булево значение (True/False). Изначально все клетки закрыты (False).
#
#
#
# С помощью класса GamePole должна быть возможность создавать квадратное игровое поле с числом клеток N x N:
#
# pole_game = GamePole(N, M)
# Здесь N - размер поля; M - общее число мин на поле. При этом, каждая клетка представляется объектом
# класса Cell и все объекты хранятся в двумерном списке N x N элементов - локальном свойстве pole объекта
# класса GamePole.
#
# В классе GamePole должны быть также реализованы следующие методы:
#
# init() - инициализация поля с новой расстановкой M мин (случайным образом по игровому полю, разумеется
# каждая мина должна находиться в отдельной клетке).
# show() - отображение поля в консоли в виде таблицы чисел открытых клеток (если клетка не открыта,
# то отображается символ #; мина отображается символом *; между клетками при отображении ставить пробел).
#
# При создании экземпляра класса GamePole в его инициализаторе следует вызывать метод init() для
# первоначальной инициализации игрового поля.
#
# В классе GamePole могут быть и другие вспомогательные методы.
#
# Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и числом мин M = 12.
#
# P.S. На экран в программе ничего выводить не нужно.


import random


class Cell:
    def __init__(self, mine: bool):
        self.around_mines = 0
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, n, m):
        self.m = m
        self.n = n
        self.pole = [[Cell(False) for _ in range(n)] for i in range(n)]
        self.init()
        self.get_count_mine()

    def init(self):
        fl = self.m
        while fl > 0:
            ind = random.randint(0, self.n - 1)
            val = random.randint(0, self.n - 1)
            if self.pole[ind][val].mine is False:
                self.pole[ind][val].mine = True
                fl = fl - 1

    def show(self):
        for i, row in enumerate(self.pole):
            for ind, val in enumerate(row):
                if val.mine is True:
                    self.pole[i][ind] = '*'
                elif val.fl_open is False:
                    self.pole[i][ind] = self.pole[i][ind].around_mines
        for i in self.pole:
            print(*i, sep=' ')

    def get_count_mine(self):
        t = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for i in range(self.n):
            for j in range(self.n):
                if not self.pole[i][j].mine:
                    mines = sum((self.pole[x+i][y+j].mine for x, y in t if 0 <= x+i < self.n and 0 <= y+j < self.n))
                    self.pole[i][j].around_mines = mines


pole_game = GamePole(10, 12)
pole_game.show()
