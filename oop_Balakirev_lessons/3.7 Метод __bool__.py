# Подвиг 4. Объявите в программе класс Player (игрок), объекты которого создаются командой:
#
# player = Player(name, old, score)
# где name - имя игрока (строка); old - возраст игрока (целое число); score - набранные очки в игре (целое число).
# В каждом объекте класса Player должны создаваться аналогичные локальные атрибуты: name, old, score.
#
# С объектами класса Player должна работать функция:
#
# bool(player)
# которая возвращает True, если число очков больше нуля, и False - в противном случае.
#
# С помощью команды:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# считываются строки из входного потока в список строк lst_in. Каждая строка записана в формате:
#
# "имя; возраст; очки"
#
# Например:
#
# Балакирев; 34; 2048
# Mediel; 27; 0
# Влад; 18; 9012
# Nina P; 33; 0
#
# Каждую строку списка lst_in необходимо представить в виде объекта класса Player с соответствующими данными.
# И из этих объектов сформировать список players.
#
# Отфильтруйте этот список (создайте новый: players_filtered), оставив всех игроков с числом очков больше нуля.
# Используйте для этого стандартную функцию filter() совместно с функцией bool() языка Python.
#
# P.S. На экран ничего выводить не нужно.


import sys


class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __repr__(self):
        return f'Фамилия: {self.name} Возраст: {self.old} Очки: {self.score}'

    def __bool__(self):
        return int(self.score) != 0


lst_in = list(map(str.strip, sys.stdin.readlines()))
players = [Player(*x.split(';')) for x in lst_in]
players_filtered = list(filter(bool, players))
print(players_filtered)


# Подвиг 5. Объявите в программе класс MailBox (почтовый ящик), объекты которого создаются командой:
#
# mail = MailBox()
# Каждый объект этого класса должен содержать локальный публичный атрибут:
#
# inbox_list - список из принятых писем.
#
# Также в классе MailBox должен присутствовать метод:
#
# receive(self) - прием новых писем
#
# Этот метод должен читать данные из входного потока командой:
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# В результате формируется список lst_in из строк. Каждая строка записана в формате:
#
# "от кого; заголовок; текст письма"
#
# Например:
#
# sc_lib@list.ru; От Балакирева; Успехов в IT!
# mail@list.ru; Выгодное предложение; Вам одобрен кредит.
# mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.
#
# Каждая строчка списка lst_in должна быть представлена объектом класса MailItem, объекты которого создаются
# командой:
#
# item = MailItem(mail_from, title, content)
# где mail_from - email отправителя (строка); title - заголовок письма (строка), content - содержимое письма
# (строка). В каждом объекте класса MailItem должны формироваться соответствующие локальные атрибуты
# (с именами: mail_from, title, content). И дополнительно атрибут is_read (прочитано ли) с начальным значением
# False.
#
# В классе MailItem должен быть реализован метод:
#
# set_read(self, fl_read) - для отметки, что письмо прочитано (метод должен устанавливать атрибут is_read =
# fl_read, если True, то письмо прочитано, если False, то не прочитано).
#
# С каждым объектом класса MailItem должна работать функция:
#
# bool(item)
# которая возвращает True для прочитанного письма и False для непрочитанного.
#
# Вызовите метод:
#
# mail.receive()
# Отметьте первое и последнее письмо в списке mail.inbox_list, как прочитанное (используйте для этого метод
# set_read). Затем, сформируйте в программе список (глобальный) с именем inbox_list_filtered из прочитанных
# писем, используя стандартную функцию filter() совместно с функцией bool() языка Python.
#
# P.S. На экран ничего выводить не нужно.
#
# Sample Input:
#
# sc_lib@list.ru; От Балакирева; Успехов в IT!
# mail@list.ru; Выгодное предложение; Вам одобрен кредит.
# mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.
# Sample Output:


import sys


class MailBox:
    def __init__(self):
        self.inbox_list = []

    def receive(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        self.inbox_list += [MailItem(*x.split(';')) for x in lst_in]


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def __repr__(self):
        return f'Статус: {'прочитано' if self.is_read else "не прочитано"}'

    def set_read(self, fl_read):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read


mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
inbox_list_filtered = list(filter(bool, mail.inbox_list))
print(mail.inbox_list)


# Подвиг 6 (релакс). Объявите класс Line, объекты которого создаются командой:
#
# line = Line(x1, y1, x2, y2)
# где x1, y1, x2, y2 - координаты начала линии (x1, y1) и координаты конца линии (x2, y2).
# Могут быть произвольными числами. В объектах класса Line должны создаваться соответствующие локальные
# атрибуты с именами x1, y1, x2, y2.
#
# В классе Line определить магический метод __len__() так, чтобы функция:
#
# bool(line)
# возвращала False, если длина линии меньше 1.
#
# P.S. На экран ничего выводить не нужно. Только объявить класс.


# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#     def __len__(self):
#         return ((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5 >= 1


# Подвиг 7. Объявите класс Ellipse (эллипс), объекты которого создаются командами:
#
# el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
# el2 = Ellipse(x1, y1, x2, y2)
# где x1, y1 - координаты (числа) левого верхнего угла; x2, y2 - координаты (числа) нижнего правого угла.
# Первая команда создает объект класса Ellipse без локальных атрибутов x1, y1, x2, y2. Вторая команда создает
# объект с локальными атрибутами x1, y1, x2, y2 и соответствующими переданными значениями.
#
# В классе Ellipse объявите магический метод __bool__(), который бы возвращал True, если все локальные атрибуты
# x1, y1, x2, y2 существуют и False - в противном случае.
#
# Также в классе Ellipse нужно реализовать метод:
#
# get_coords() - для получения кортежа текущих координат объекта.
#
# Если координаты отсутствуют (нет локальных атрибутов x1, y1, x2, y2), то метод get_coords() должен генерировать
# исключение командой:
#
# raise AttributeError('нет координат для извлечения')
# Сформируйте в программе список с именем lst_geom, содержащий четыре объекта класса Ellipse. Два объекта должны
# быть созданы командой
#
# Ellipse()
# и еще два - командой:
#
# Ellipse(x1, y1, x2, y2)
# Переберите список в цикле и вызовите метод get_coords() только для объектов, имеющих координаты x1, y1, x2, y2.
# (Помните, что для этого был определен магический метод __bool__()).
#
# P.S. На экран ничего выводить не нужно.


class Ellipse:
    def __init__(self, *args):
        if len(args) == 4:
            self.x1, self.y1, self.x2, self.y2 = args

    def __bool__(self):
        return len(self.__dict__) != 0

    def get_coords(self):
        if len(self.__dict__) == 0:
            raise AttributeError('нет координат для извлечения')
        return self.x1, self.y1, self.x2, self.y2


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
for i in lst_geom:
    if i:
        i.get_coords()


# Большой подвиг 8. Вы начинаете разрабатывать игру "Сапер". Для этого вам нужно уметь представлять и управлять
# игровым полем. Будем полагать, что оно имеет размеры N x M клеток. Каждая клетка будет представлена объектом
# класса Cell и содержать либо число мин вокруг этой клетки, либо саму мину.
#
#
#
# Для начала в программе объявите класс GamePole, который будет создавать и управлять игровым полем. Объект этого
# класса должен формироваться командой:
#
# pole = GamePole(N, M, total_mines)
# И, так как поле в игре одно, то нужно контролировать создание только одного объекта класса GamePole (используйте
# паттерн Singleton, о котором мы с вами говорили, когда рассматривали магический метод __new__()).
#
# Объект pole должен иметь локальный приватный атрибут:
#
# __pole_cells - двумерный (вложенный) кортеж, размерами N x M элементов (N строк и M столбцов), состоящий из
# объектов класса Cell.
#
# Для доступа к этой коллекции объявите в классе GamePole объект-свойство (property):
#
# pole - только для чтения (получения) ссылки на коллекцию __pole_cells.
#
# Далее, в самом классе GamePole объявите следующие методы:
#
# init_pole() - для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми);
# open_cell(i, j) - открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля; метод меняет значение
# атрибута __is_open объекта Cell в ячейке (i, j) на True;
# show_pole() - отображает игровое поле в консоли (как именно сделать - на ваше усмотрение, этот метод - домашнее
# задание).
#
# Расстановку мин выполняйте случайным образом по игровому полю (для этого удобно воспользоваться функцией randint
# модуля random). После расстановки всех total_mines мин, вычислите их количество вокруг остальных клеток
# (где нет мин).
# Область охвата - соседние (прилегающие) клетки (8 штук).
#
# В методе open_cell() необходимо проверять корректность индексов (i, j). Если индексы указаны некорректно,
# то генерируется исключение командой:
#
# raise IndexError('некорректные индексы i, j клетки игрового поля')
# Следующий класс Cell описывает состояние одной ячейки игрового поля. Объекты этого класса создаются командой:
#
# cell = Cell()
# При этом в самом объекте создаются следующие локальные приватные свойства:
#
# __is_mine - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
# __number - число мин вокруг клетки (целое число от 0 до 8);
# __is_open - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.
#
# Для работы с этими приватными атрибутами объявите в классе Cell следующие объекты-свойства с именами:
#
# is_mine - для записи и чтения информации из атрибута __is_mine;
# number - для записи и чтения информации из атрибута __number;
# is_open - для записи и чтения информации из атрибута __is_open.
#
# В этих свойствах необходимо выполнять проверку на корректность переданных значений (либо булево значение True/False,
# либо целое число от 0 до 8). Если передаваемое значение некорректно, то генерировать исключение командой:
#
# raise ValueError("недопустимое значение атрибута")
# С объектами класса Cell должна работать функция:
#
# bool(cell)
# которая возвращает True, если клетка закрыта и False - если открыта.
#
# Пример использования классов (эти строчки в программе писать не нужно):
#
# pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
# pole.init_pole()
# if pole.pole[0][1]:
#     pole.open_cell(0, 1)
# if pole.pole[3][5]:
#     pole.open_cell(3, 5)
# pole.open_cell(30, 100)  # генерируется исключение IndexError
# pole.show_pole()
# P.S. В программе на экран выводить ничего не нужно, только объявить классы.


from random import randint


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, N, M, total_mines):
        self.n = N
        self.m = M
        self.total_mines = total_mines
        self.__pole_cells = tuple((Cell(),) * self.n for _ in range(self.m))

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        while self.total_mines:
            ind = randint(0, self.n - 1)
            val = randint(0, self.m - 1)
            if not self.pole[ind][val].is_mine:
                self.pole[ind][val].is_mine = True
                self.total_mines -= 1


        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.n):
            for y in range(self.m):
                self.pole[x][y].is_open = False
                if not self.pole[x][y].is_mine:
                    mines = sum((self.pole[x+i][y+j].is_mine for i, j in indx if 0 <= i <= self.n and 0 <= j <= self.m))
                    self.pole[x][y].number = mines

    def open_cell(self, i, j):
        if not 0 <= i <= self.n and not 0 <= j <= self.m:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self):
        for i in self.pole:
            print(*i)


class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = None
        self.__is_open = None

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value):
        self.__is_valid_value(value)
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__is_valid_value(value)
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        self.__is_valid_value(value)
        self.__is_open = value

    @staticmethod
    def __is_valid_value(value):
        if not type(value) is bool or type(value) == int and 0 <= value <= 8:
            raise ValueError("недопустимое значение атрибута")

    def __bool__(self):
        return self.is_open is False

    def __repr__(self):
        return '*'


pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()


# Подвиг 9 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:
#
# v = Vector(x1, x2, x3,..., xN)
# где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).
#
# С каждым объектом класса Vector должны выполняться операторы:
#
# v1 + v2 # суммирование соответствующих координат векторов
# v1 - v2 # вычитание соответствующих координат векторов
# v1 * v2 # умножение соответствующих координат векторов
#
# v1 += 10 # прибавление ко всем координатам вектора числа 10
# v1 -= 10 # вычитание из всех координат вектора числа 10
# v1 += v2
# v2 -= v1
#
# v1 == v2 # True, если соответствующие координаты векторов равны
# v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
# При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными)
# координатами. При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.
#
# Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться
# исключение командой:
#
# raise ArithmeticError('размерности векторов не совпадают')
# P.S. В программе на экран выводить ничего не нужно, только объявить класс.


class Vector:
    def __init__(self, *args):
        self.coord = list(args)

    @staticmethod
    def __valid_len_coords(v1, v2):
        if len(v1) != len(v2):
            raise ArithmeticError('размерности векторов не совпадают')

    @staticmethod
    def __get_values(lst1, lst2):
        return zip(lst1, lst2)

    def __add__(self, other):
        self.__valid_len_coords(self.coord, other.coord)
        lst = self.__get_values(self.coord, other.coord)
        return Vector(*map(lambda x: x[0] + x[1], lst))

    def __sub__(self, other):
        self.__valid_len_coords(self.coord, other.coord)
        lst = self.__get_values(self.coord, other.coord)
        return Vector(*map(lambda x: x[0] - x[1], lst))

    def __mul__(self, other):
        self.__valid_len_coords(self.coord, other.coord)
        lst = self.__get_values(self.coord, other.coord)
        return Vector(*map(lambda x: x[0] * x[1], lst))

    def __iadd__(self, other):
        sc = other
        if not isinstance(other, Vector):
            sc = Vector(*[other for _ in range(len(self.coord))])
        self.__valid_len_coords(self.coord, sc.coord)
        lst = self.__get_values(self.coord, sc.coord)
        self.coord = list(map(lambda x: x[0] + x[1], lst))
        return self

    def __isub__(self, other):
        sc = other
        if not isinstance(other, Vector):
            sc = Vector(*[other for _ in range(len(self.coord))])
        self.__valid_len_coords(self.coord, sc.coord)
        lst = self.__get_values(self.coord, sc.coord)
        self.coord = list(map(lambda x: x[0] - x[1], lst))
        return self

    def __eq__(self, other):
        self.__valid_len_coords(self.coord, other.coord)
        lst = self.__get_values(self.coord, other.coord)
        return all((map(lambda x: x[0] == x[1], lst)))


