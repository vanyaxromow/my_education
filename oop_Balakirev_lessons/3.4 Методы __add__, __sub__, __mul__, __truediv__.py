# Подвиг 4. Известно, что в Python мы можем соединять два списка между собой с помощью оператора +:
#
# lst = [1, 2, 3] + [4.5, -3.6, 0.78]
# Но нет реализации оператора -, который бы убирал из списка соответствующие значения вычитаемого списка,
# как это показано в примере:
#
# lst = [1, 2, 3, 4, 5, 6] - [5, 6, 7, 8, 1] # [2, 3, 4] (порядок следования оставшихся элементов списка должен
# # сохраняться)
# Давайте это поправим и создадим такой функционал. Для этого нужно объявить класс с именем NewList, объекты
# которого создаются командами:
#
# lst = NewList() # пустой список
# lst = NewList([-1, 0, 7.56, True]) # список с начальными значениями
# Реализуйте для этого класса работу с оператором вычитания, чтобы над объектами класса NewList можно было
# выполнять следующие действия:
#
# lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
# lst2 = NewList([0, 1, 2, 3, True])
# res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
# lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
# res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
# res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
# Также в классе NewList необходимо объявить метод:
#
# get_list() - для возвращения результирующего списка объекта класса NewList
#
# Например:
#
# lst = res_2.get_list() # [1, 2, 3]
# P.S. В программе требуется только объявить класс. На экран ничего выводить не нужно.


class NewList:
    def __init__(self, lst=None):
        self._lst = lst[:] if lst and type(lst) == list else []

    def get_list(self):
        return self._lst

    def __sub__(self, other):
        if type(other) not in (list, NewList):
            raise ArithmeticError('Правый операнд должен быть list или NewList')
        other_list = other if type(other) == list else other.get_list()
        return NewList(self.__diff_list(self._lst, other_list))

    def __rsub__(self, other):
        if type(other) != list:
            raise ArithmeticError('Правый операнд должен быть list')
        return NewList(self.__diff_list(other, self._lst))

    @staticmethod
    def __diff_list(lst1, lst2):
        if len(lst2) == 0:
            return lst1

        sub = lst2[:]
        return [x for x in lst1 if not NewList.__is_elem(x, sub)]

    @staticmethod
    def __is_elem(x, sub):
        res = any(map(lambda xx: type(x) == type(xx) and x == xx, sub))
        if res:
            sub.remove(x)
        return res


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
res_2 = lst2 - [0, True] # NewList: [1, 2, 3]
res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]


# Подвиг 5. Объявите класс с именем ListMath, объекты которого можно создавать командами:
#
# lst1 = ListMath() # пустой список
# lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями
# В качестве значений элементов списка объекты класса ListMath должны отбирать только целые и вещественные числа,
# остальные игнорировать (если указываются в списке). Например:
#
# lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
# В каждом объекте класса ListMath должен быть публичный атрибут:
#
# lst_math - ссылка на текущий список объекта (для каждого объекта создается свой список).
#
# Также с объектами класса ListMath должны работать следующие операторы:
#
# lst = lst + 76 # сложение каждого числа списка с определенным числом
# lst = 6.5 + lst # сложение каждого числа списка с определенным числом
# lst += 76.7  # сложение каждого числа списка с определенным числом
# lst = lst - 76 # вычитание из каждого числа списка определенного числа
# lst = 7.0 - lst # вычитание из числа каждого числа списка
# lst -= 76.3
# lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
# lst *= 5.54
# lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
# lst = 3 / lst # деление числа на каждый элемент списка
# lst /= 13.0
# При использовании бинарных операторов +, -, *, / должны формироваться новые объекты класса ListMath с новыми
# списками, прежние списки не меняются.
#
# При использовании операторов +=, -=, *=, /= значения должны меняться внутри списка текущего объекта
# (новый объект не создается).
#
# P.S. В программе достаточно только объявить класс. На экран ничего выводить не нужно.


class ListMath:
    def __init__(self, lst=None):
        self.lst_math = [x for x in ListMath.__is_valid(lst)] if lst else []

    @staticmethod
    def __is_valid(lst):
        res = [x for x in lst if type(x) in (int, float)]
        return res

    @staticmethod
    def __is_verify(other):
        if type(other) not in (int, float):
            raise ArithmeticError('Операнд должен быть числом')

    def __add__(self, other):
        self.__is_verify(other)
        return ListMath([x + other for x in self.lst_math])

    def __radd__(self, other):
        self.__is_verify(other)
        return self.__add__(other)

    def __iadd__(self, other):
        self.__is_verify(other)
        self.lst_math = [x + other for x in self.lst_math]
        return self

    def __sub__(self, other):
        self.__is_verify(other)
        return ListMath([x - other for x in self.lst_math])

    def __rsub__(self, other):
        self.__is_verify(other)
        return ListMath([other - x for x in self.lst_math])

    def __isub__(self, other):
        self.__is_verify(other)
        self.lst_math = [x - other for x in self.lst_math]
        return self

    def __mul__(self, other):
        self.__is_verify(other)
        return ListMath([x * other for x in self.lst_math])

    def __rmul__(self, other):
        self.__is_verify(other)
        return ListMath([x * other for x in self.lst_math])

    def __imul__(self, other):
        self.__is_verify(other)
        self.lst_math = [x * other for x in self.lst_math]
        return self

    def __truediv__(self, other):
        self.__is_verify(other)
        return ListMath([x / other for x in self.lst_math])

    def __rtruediv__(self, other):
        self.__is_verify(other)
        return self.__truediv__(other)

    def __itruediv__(self, other):
        self.__is_verify(other)
        self._lst = [x / other for x in self.lst_math]
        return self


# Подвиг 6. Ранее, в одном из подвигов мы с вами создавали односвязный список с объектами класса StackObj
# (когда один объект ссылается на следующий и так далее):

# Давайте снова создадим такую структуру данных. Для этого объявим два класса:
#
# Stack - для управления односвязным списком в целом;
# StackObj - для представления отдельных объектов в односвязным списком.
#
# Объекты класса StackObj должны создаваться командой:
#
# obj = StackObj(data)
# где data - строка с некоторыми данными.
#
# Каждый объект класса StackObj должен иметь локальные приватные атрибуты:
#
# __data - ссылка на строку с переданными данными;
# __next - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None).
#
# Объекты класса Stack создаются командой:
#
# st = Stack()
# и каждый из них должен содержать локальный атрибут:
#
# top - ссылка на первый объект односвязного списка (если объектов нет, то top = None).
#
# Также в классе Stack следует объявить следующие методы:
#
# push_back(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
# pop_back(self) - удаление последнего объекта из односвязного списка.
#
# Дополнительно нужно реализовать следующий функционал
# (в этих операциях копии односвязного списка создавать не нужно):
#
# # добавление нового объекта класса StackObj в конец односвязного списка st
# st = st + obj
# st += obj
#
# # добавление нескольких объектов в конец односвязного списка
# st = st * ['data_1', 'data_2', ..., 'data_N']
# st *= ['data_1', 'data_2', ..., 'data_N']
# В последних двух строчках должны автоматически создаваться N объектов класса StackObj с данными, взятыми из списка
# (каждый элемент списка для очередного добавляемого объекта).

# P.S. В программе достаточно только объявить классы. На экран ничего выводить не нужно.


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, obj):
        self.__data = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj


class Stack:
    def __init__(self):
        self.top = None

    @property
    def top(self):
        return self.__top

    @top.setter
    def top(self, value):
        self.__top = value

    def push_back(self, obj):
        """ Добавление объекта класса StackObj в конец односвязного списка"""
        if not self.top:
            self.top = obj
            return
        ptr = self.top
        while ptr.next:
            ptr = ptr.next
        ptr.next = obj
        return self


    def pop_back(self):
        """Удаление последнего объекта из односвязного списка"""
        if not self.top:
            return None
        ptr = self.top if self.top else None
        prev = None
        while ptr.next:
            prev = ptr
            ptr = ptr.next
        prev.next = None

    @staticmethod
    def __is_verify_obj(obj):
        if not isinstance(obj, StackObj):
            raise ValueError('Операнд должен быть объектом StackObj')

    def __add__(self, other):
        self.__is_verify_obj(other)
        return self.push_back(other)

    def __mul__(self, other):
        if not isinstance(other, list):
            raise ValueError('Операнд должен быть списком')
        res = [self.push_back(StackObj(x)) for x in other]
        return self

    def __imul__(self, other):
        if not isinstance(other, list):
            raise ValueError('Операнд должен быть списком')
        return self * other


# Подвиг 7. Вам поручается создать программу по учету книг (библиотеку). Для этого необходимо в программе
# объявить два класса:
#
# Lib - для представления библиотеки в целом;
# Book - для описания отдельной книги.
#
# Объекты класса Book должны создаваться командой:
#
# book = Book(title, author, year)
# где title - заголовок книги (строка); author - автор книги (строка); year - год издания (целое число).
#
# Объекты класса Lib создаются командой:
#
# lib = Lib()
# Каждый объект должен содержать локальный публичный атрибут:
#
# book_list - ссылка на список из книг (объектов класса Book). Изначально список пустой.
#
# Также объекты класса Lib должны работать со следующими операторами:
#
# lib = lib + book # добавление новой книги в библиотеку
# lib += book
#
# lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book
# # класса Book)
# lib -= book
#
# lib = lib - indx # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
# lib -= indx
# При реализации бинарных операторов + и - создавать копии библиотек (объекты класса Lib) не нужно.
#
# Также с объектами класса Lib должна работать функция:
#
# n = len(lib) # n - число книг
# которая возвращает число книг в библиотеке.
#
# P.S. В программе достаточно только объявить классы. На экран ничего выводить не нужно.


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list = []

    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if isinstance(other, Book):
            self.book_list.remove(other)
        elif isinstance(other, int):
            self.book_list.pop(other)
        return self

    def __len__(self):
        return len(self.book_list)


# Подвиг 8. Вам необходимо создать простую программу по учету семейного бюджета. Для этого в программе объявите
# два класса с именами:
#
# Budget - для управления семейным бюджетом;
# Item - пункт расходов бюджета.
#
# Объекты класса Item должны создаваться командой:
#
# it = Item(name, money)
# где name - название статьи расхода; money - сумма расходов (вещественное или целое число).
#
# Соответственно, в каждом объекте класса Item должны формироваться локальные атрибуты name и money с переданными
# значениями. Также с объектами класса Item должны выполняться следующие операторы:
#
# s = it1 + it2 # сумма для двух статей расходов
# и в общем случае:
#
# s = it1 + it2 + ... + itN # сумма N статей расходов
# При суммировании оператор + должен возвращать число - вычисленную сумму по атрибутам money соответствующих
# объектов класса Item.
#
# Объекты класса Budget создаются командой:
#
# my_budget = Budget()
# А сам класс Budget должен иметь следующие методы:
#
# add_item(self, it) - добавление статьи расхода в бюджет (it - объект класса Item);
# remove_item(self, indx) - удаление статьи расхода из бюджета по его порядковому номеру indx (индексу:
# отсчитывается с нуля);
# get_items(self) - возвращает список всех статей расходов (список из объектов класса Item).
#
# Пример использования классов (эти строчки в программе писать не нужно):
#
# my_budget = Budget()
# my_budget.add_item(Item("Курс по Python ООП", 2000))
# my_budget.add_item(Item("Курс по Django", 5000.01))
# my_budget.add_item(Item("Курс по NumPy", 0))
# my_budget.add_item(Item("Курс по C++", 1500.10))
#
# # вычисление общих расходов
# s = 0
# for x in my_budget.get_items():
#     s = s + x
# P.S. В программе требуется только объявить класс. На экран ничего выводить не нужно.


class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        return self.money + other

    def __radd__(self, other):
        return self.__add__(other)


class Budget:
    def __init__(self):
        self.items = []

    def add_item(self, it):
        self.items.append(it)

    def remove_item(self, indx):
        if type(indx) == int and indx > len(self.items):
            self.items.pop(indx)

    def get_items(self):
        return self.items


# Подвиг 9. Объявите класс Box3D для представления прямоугольного параллелепипеда (бруска), объекты которого
# создаются командой:
#
# box = Box3D(width, height, depth)
# где width, height, depth - ширина, высота и глубина соответственно (числа: целые или вещественные)
#
# В каждом объекте класса Box3D должны создаваться публичные атрибуты:
#
# width, height, depth - ширина, высота и глубина соответственно.
#
# С объектами класса Box3D должны выполняться следующие операторы:
#
# box1 = Box3D(1, 2, 3)
# box2 = Box3D(2, 4, 6)
#
# box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
# box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
# box = 3 * box2    # Box3D: width=6, height=12, depth=18
# box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
# box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
# box = box2 % 3    # Box3D: width=2, height=1, depth=0
# При каждой арифметической операции следует создавать новый объект класса Box3D с соответствующими значениями
# локальных атрибутов.
#
# P.S. В программе достаточно только объявить класс Box3D. На экран ничего выводить не нужно.


class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        if isinstance(other, Box3D):
            return Box3D(self.width+other.width, self.height+other.height, self.depth+other.depth)

    def __mul__(self, other):
        if isinstance(other, int):
            return Box3D(self.width*other, self.height*other, self.depth*other)

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        if isinstance(other, Box3D):
            return Box3D(self.width-other.width, self.height-other.height, self.depth-other.depth)

    def __floordiv__(self, other):
        if isinstance(other, int):
            return Box3D(self.width // other, self.height // other, self.depth // other)

    def __mod__(self, other):
        if isinstance(other, int):
            return Box3D(self.width % other, self.height % other, self.depth % other)


# Подвиг 10 (на повторение). В нейронных сетях использую операцию под названием Max Pooling.
# Суть ее состоит в сканировании прямоугольной таблицы чисел (матрицы) окном определенного размера
# (обычно, 2x2 элемента) и выбора наибольшего значения в пределах этого окна:

#  Или, если окна выходят за пределы матрицы, то они пропускаются (игнорируются):
#
# Мы повторим эту процедуру. Для этого в программе нужно объявить класс с именем MaxPooling, объекты которого
# создаются командой:
#
# mp = MaxPooling(step=(2, 2), size=(2,2))
# где step - шаг смещения окна по горизонтали и вертикали; size - размер окна по горизонтали и вертикали.
#
# Параметры step и size по умолчанию должны принимать кортеж со значениями (2, 2).
#
# Для выполнения операции Max Pooling используется команда:
#
# res = mp(matrix)
# где matrix - прямоугольная таблица чисел; res - ссылка на результат обработки таблицы matrix
# (должна создаваться новая таблица чисел.
#
# Прямоугольную таблицу чисел следует описывать вложенными списками. Если при сканировании таблицы часть окна
# выходит за ее пределы, то эти данные отбрасывать (не учитывать все окно).
#
# Если matrix не является прямоугольной таблицей или содержит хотя бы одно не числовое значение, то должно
# генерироваться исключение командой:
#
# raise ValueError("Неверный формат для первого параметра matrix.")
# Пример использования класса (эти строчки в программе писать не нужно):
#
# mp = MaxPooling(step=(2, 2), size=(2,2))
# res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
# Результатом будет таблица чисел:
#
# 6 8
# 9 7
#
# P.S. В программе достаточно объявить только класс. Выводить на экран ничего не нужно.


class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.__step = step
        self.__size = size

    def __call__(self, matrix):
        rows = len(matrix)  # количество строк
        cols = len(matrix[0]) if rows > 0 else 0  # количество столбцов

        if rows == 0:  # если кол-во строк = 0, то возвратим пустую матрицу
            return [[]]

        # проверим, что матрица является прямоугольной таблицей и таблицей именно чисел
        if not all(map(lambda x: len(x) == cols, matrix)) or \
                not all(map(lambda row: all(map(lambda x: type(x) in (int, float), row)), matrix)):
            raise ValueError("Неверный формат для первого параметра matrix.")

        h, w = self.__size[0], self.__size[1]
        sh, sw = self.__step[0], self.__step[1]

        # подсчитаем, какое кол-во окон будет при сканировании матрицы по строкам и столбцам
        rows_range = (rows - h) // sh + 1
        cols_range = (cols - w) // sw + 1

        # сформируем выходную матрицу, которая изначально будет состоять из нулей
        res = [[0] * cols_range for _ in range(rows_range)]

        # Max Pooling
        for i in range(rows_range):
            for j in range(cols_range):
                s = (x for r in matrix[i * sh: i * sh + h] for x in r[j * sw: j * sw + w])
                res[i][j] = max(s)

        return res


mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
print(res)
