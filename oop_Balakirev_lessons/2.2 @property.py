from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшзъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)

        self.__fio = fio.split()
        self.old = old
        self.ps = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        """ Проверка корректности ФИО """
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')

        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат записи')

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('В ФИО должен быть хотя бы один символ')
            if len(s.strip(letters)) != 0:
                raise TypeError('В ФИО можно использовать только буквенные символы и дефис')

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('Возраст должен быть целым числом и в диапазоне [14;120]')

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 14 or w > 120:
            raise TypeError('Вес должен быть вещественным числом от 20 и выше')

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('Паспорт должен быть записан в виде строки')

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Неверный формат записи')

        for p in s:
            if not p.isdigit():
                raise TypeError('Серия и номер паспорта должны быть числами')

    @property
    def fio(self):
        """ Для фио прописываем только геттер """
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__ps

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__ps = ps


p = Person('Балакирев Сергей Михайлович', 30, '1234 567890', 80.0)
p.old = 40
p.passport = '5678 123456'
p.weight = 100.0
print(p.__dict__)


# Подвиг 4. Объявите в программе класс Car, в котором реализуйте объект-свойство с именем model для записи
# и считывания информации о модели автомобиля из локальной приватной переменной __model.
#
# Объект-свойство объявите с помощью декоратора @property. Также в объекте-свойстве model должны быть реализованы
# проверки:
#
# - модель автомобиля - это строка;
# - длина строки модели должна быть в диапазоне [2; 100].
#
# Если проверка не проходит, то локальное свойство __model остается без изменений.
#
# Объекты класса Car предполагается создавать командой:
#
# car = Car()
# и далее работа с объектом-свойством, например:
#
# car.model = "Toyota"
# P.S. В программе объявить только класс. На экран ничего выводить не нужно.


class Car:
    def __init__(self, model=None):
        self.__model = model

    @classmethod
    def verify_model(cls, model):
        return type(model) == str and 2 <= len(model) <= 100

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.verify_model(model):
           self.__model = model


# Подвиг 5. Объявите в программе класс WindowDlg, объекты которого предполагается создавать командой:
#
# wnd = WindowDlg(заголовок окна, ширина, высота)
# В каждом объекте класса WindowDlg должны создаваться приватные локальные атрибуты:
#
# __title - заголовок окна (строка);
# __width, __height - ширина и высота окна (числа).
#
# В классе WindowDlg необходимо реализовать метод:
#
# show() - для отображения окна на экране (выводит в консоль строку в формате: "<Заголовок>: <ширина>, <высота>",
# например "Диалог 1: 100, 50").
#
# Также в классе WindowDlg необходимо реализовать два объекта-свойства:
#
# width - для изменения и считывания ширины окна;
# height - для изменения и считывания высоты окна.
#
# При изменении размеров окна необходимо выполнять проверку:
#
# - переданное значение является целым числом в диапазоне [0; 10000].
#
# Если хотя бы один размер изменился (высота или ширина), то следует выполнить автоматическую перерисовку окна
# (вызвать метод show()). При начальной инициализации размеров width, height вызывать метод show() не нужно.
#
# P.S. В программе нужно объявить только класс с требуемой функциональностью.


class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.__title}: {self.width}, {self.height}")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int and 0 <= value <= 10000:
            self.__width = value
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int and 0 <= value <= 100:
            self.__height = value
            self.show()


# Подвиг 6. Реализуйте односвязный список (не список Python, не использовать список Python для хранения объектов),
# когда один объект ссылается на следующий и так по цепочке до последнего:
#
#
#
# Для этого объявите в программе два класса:
#
# StackObj - для описания объектов односвязного списка;
# Stack - для управления односвязным списком.
#
# Объекты класса StackObj предполагается создавать командой:
#
# obj = StackObj(данные)
# Здесь данные - это строка с некоторым содержимым. Каждый объект класса StackObj должен иметь следующие
# локальные приватные атрибуты:
#
# __data - ссылка на строку с данными, указанными при создании объекта;
# __next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).
#
# Также в классе StackObj должны быть объявлены объекты-свойства:
#
# next - для записи и считывания информации из локального приватного свойства __next;
# data - для записи и считывания информации из локального приватного свойства __data.
#
# При записи необходимо реализовать проверку, что __next будет ссылаться на объект класса StackObj или
# значение None. Если проверка не проходит, то __next остается без изменений.
#
# Класс Stack предполагается использовать следующим образом:
#
# st = Stack() # создание объекта односвязного списка
# В объектах класса Stack должен быть локальный публичный атрибут:
#
# top - ссылка на первый добавленный объект односвязного списка (если список пуст, то top = None).
#
# А в самом классе Stack следующие методы:
#
# push(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
# pop(self) - извлечение последнего объекта с его удалением из односвязного списка;
# get_data(self) - получение списка из объектов односвязного списка (список из строк локального атрибута
# __data каждого объекта в порядке их добавления, или пустой список, если объектов нет).
#
# Пример использования классов Stack и StackObj (эти строчки в программе писать не нужно):
#
# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st.pop()
# res = st.get_data()    # ['obj1', 'obj2']
# P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if isinstance(value, StackObj) or value is None:
            self.__next = value


class Stack:

    def __init__(self):
        self.top = None
        self.tail = None

    def push(self, obj):
        if not self.top:
            self.top = obj

        elif not self.tail:
            self.tail = obj
            self.top.next = obj

        else:
            self.tail.next = obj
            self.tail = obj

    def pop(self):
        node = self.top
        res = None
        while node:
            if node.next is None and node is self.top:
                res = node
                self.top = None
                return res
            else:
                ptr = node.next
                if ptr.next is None:
                    res = node.next
                    node.next = None
                    self.tail = node
                    return res

            node = node.next

    def get_data(self):
        lst = []
        node = self.top
        while node:
            lst.append(node.data)
            node = node.next
        return lst


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()  # ['obj1', 'obj2']
print(res)


# Подвиг 7. Объявите класс RadiusVector2D, объекты которого должны создаваться командами:
#
# v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
# v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
# v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)
# В каждом объекте класса RadiusVector2D должны формироваться локальные приватные атрибуты:
#
# __x, __y - координаты конца вектора (изначально значения равны 0, если не передано какое-либо другое).
#
# В классе RadiusVector2D необходимо объявить два объекта-свойства:
#
# x - для изменения и считывания локального атрибута __x;
# y - для изменения и считывания локального атрибута __y.
#
# При инициализации и изменении локальных атрибутов, необходимо проверять корректность передаваемых значений:
#
# - значение должно быть числом (целым или вещественным) в диапазоне [MIN_COORD; MAX_COORD].
#
# Если проверка не проходит, то координаты не меняются (напомню, что при инициализации они изначально равны 0).
# Величины MIN_COORD = -100, MAX_COORD = 1024 задаются как публичные атрибуты класса RadiusVector2D.
#
# Также в классе RadiusVector2D необходимо объявить статический метод:
#
# norm2(vector) - для вычисления квадратической нормы vector - переданного объекта класса RadiusVector2D
# (квадратическая норма вектора: x*x + y*y).
#
# P.S. В программе требуется объявить только класс. На экран ничего выводить не нужно.


class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) in (int, float) and self.MIN_COORD <= value <= self.MAX_COORD:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) in (int, float) and self.MIN_COORD <= value <= self.MAX_COORD:
            self.__y = value

    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y


r1 = RadiusVector2D()
r2 = RadiusVector2D(1)
r3 = RadiusVector2D(4, 5)



# Большой подвиг 8. Требуется реализовать программу по работе с решающими деревьями:
#
# Здесь в каждом узле дерева делается проверка (задается вопрос). Если проверка проходит, то осуществляется
# переход к следующему объекту по левой стрелке (с единицей), а иначе - по правой стрелке (с нулем).
# И так до тех пор, пока не дойдем до одного из листа дерева (вершины без потомков).
#
# В качестве входных данных используется вектор (список) с бинарными значениями: 1 - да, 0 - нет.
# Каждый элемент этого списка соответствует своему вопросу (своей вершине дерева), например:
#
# Далее, этот вектор применяется к решающему дереву, следующим образом. Корневая вершина "Любит Python"
# с ней связан первый элемент вектора x и содержит значение 1, следовательно, мы переходим по левой ветви.
# Попадаем в вершину "Понимает ООП". С ней связан второй элемент вектора x со значением 0, следовательно,
# мы переходим по правой ветви и попадаем в вершину "будет кодером". Так как эта вершина конечная (листовая),
# то получаем результат в виде строки "будет кодером". По аналогии выполняется обработка вектора x с другими
# наборами значений 0 и 1.
#
# Для реализации решающих деревьев в программе следует объявить два класса:
#
# TreeObj - для описания вершин и листьев решающего дерева;
# DecisionTree - для работы с решающим деревом в целом.
#
# В классе DecisionTree должны быть реализованы (по крайне мере) два метода уровня класса (@classmethod):
#
# def predict(cls, root, x) - для построения прогноза (прохода по решающему дереву) для вектора x из корневого
# узла дерева root (возвращает значение узла - атрибут value).
# def add_obj(cls, obj, node=None, left=True) - для добавления вершин в решающее дерево (метод должен возвращать
# добавленную вершину - объект класса TreeObj);
#
# В методе add_obj параметры имеют, следующие значения:
#
# obj - ссылка на новый (добавляемый) объект решающего дерева (объект класса TreeObj);
# node - ссылка на объект дерева, к которому присоединяется вершина obj;
# left - флаг, определяющий ветвь дерева (объекта node), к которой присоединяется объект obj (True - к левой ветви;
# False - к правой).
#
# В классе TreeObj следует объявить инициализатор:
#
# def __init__(self, indx, value=None): ...
#
# где indx - проверяемый в вершине дерева индекс вектора x; value - значение, хранящееся в вершине
# (принимает значение None для вершин, у которых есть потомки - промежуточных вершин).
#
# При этом, в каждом создаваемом объекте класса TreeObj должны автоматически появляться следующие локальные атрибуты:
#
# indx - проверяемый индекс (целое число);
# value - значение с данными (строка);
# __left - ссылка на следующий объект дерева по левой ветви (изначально None);
# __right - ссылка на следующий объект дерева по правой ветви (изначально None).
#
# Для работы с локальными приватными атрибутами __left и __right необходимо объявить объекты-свойства с именами
# left и right.
#
# Эти классы в дальнейшем предполагается использовать следующим образом (эти строчки в программе не писать):
#
# root = DecisionTree.add_obj(TreeObj(0))
# v_11 = DecisionTree.add_obj(TreeObj(1), root)
# v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
# DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
# DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
# DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
# DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)
#
# x = [1, 1, 0]
# res = DecisionTree.predict(root, x) # будет программистом
# P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.


class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj


class DecisionTree:
    TOP_OBJ = None

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if cls.TOP_OBJ is None:
            cls.TOP_OBJ = obj

        else:
            if left is True:
                node.left = obj
            else:
                node.right = obj
        return obj

    @classmethod
    def predict(cls, root, x):
        node = cls.TOP_OBJ
        while node.left or node.right:
            if x[node.indx]:
                node = node.left
            else:
                node = node.right
        return node.value


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом
print(res)


# Подвиг 9 (на закрепление). Вам требуется сформировать класс PathLines для описания маршрутов, состоящих
# из линейных сегментов. При этом каждый линейный сегмент предполагается задавать отдельным классом LineTo.
# Объекты этого класса будут формироваться командой:
#
# line = LineTo(x, y)
# где x, y - следующая координата линейного участка (начало маршрута из точки 0, 0).
#
# В каждом объекте класса LineTo должны формироваться локальные атрибуты:
#
# x, y - для хранения координат конца линии (начало определяется по координатам предыдущего объекта).
#
# Объекты класса PathLines должны создаваться командами:
#
# p = PathLines()                   # начало маршрута из точки 0, 0
# p = PathLines(line1, line2, ...)  # начало маршрута из точки 0, 0
# где line1, line2, ... - объекты класса LineTo.
#
# Сам же класс PathLines должен иметь следующие методы:
#
# get_path() - возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
# get_length() - возвращает суммарную длину пути (сумма длин всех линейных сегментов);
# add_line(self, line) - добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.
#
# Пояснение: суммарный маршрут - это сумма длин всех линейных сегментов, а длина каждого линейного сегмента
# определяется как евклидовое расстояние по формуле:
#
# L = sqrt((x1-x0)^2 + (y1-y0)^2)
#
# где x0, y0 - предыдущая точка маршрута; x1, y1 - текущая точка маршрута.
#
# Пример использования классов (эти строчки в программе писать не нужно):
#
# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
# dist = p.get_length()
# P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.


class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.coords = list((LineTo(0, 0),) + args)

    def get_path(self):
        return self.coords[1:]

    def get_length(self):
        g = ((self.coords[i - 1], self.coords[i]) for i in range(1, len(self.coords)))
        return sum(map(lambda t: ((t[0].x - t[1].x) ** 2 + (t[0].y - t[1].y) ** 2) ** 0.5, g))

    def add_line(self, line):
        self.coords.append(line)


p = PathLines(LineTo(1, 2))
print(p.get_length())  # 2.23606797749979

p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
print(p.get_length())  # 28.191631669843197
m = p.get_path()
print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True
#
h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
print(h.get_length())  # 71.8992593599813
#
k = PathLines()
print(k.get_length())  # 0
print(k.get_path())  # []


# Подвиг 10 (на закрепление). Вы создаете телефонную записную книжку. Она определяется классом PhoneBook.
# Объекты этого класса создаются командой:
#
# p = PhoneBook()
# А сам класс должен иметь следующий набор методов:
#
# add_phone(phone) - добавление нового номера телефона (в список);
# remove_phone(indx) - удаление номера телефона по индексу списка;
# get_phone_list() - получение списка из объектов всех телефонных номеров.
#
# Каждый номер телефона должен быть представлен классом PhoneNumber. Объекты этого класса должны создаваться командой:
#
# note = PhoneNumber(number, fio)
# где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра);
# fio - Ф.И.О. владельца номера (строка).
#
# В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:
#
# number - номер телефона (число);
# fio - ФИО владельца номера телефона.
#
# Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии с заданием.
#
# Пример использования классов (эти строчки в программе писать не нужно):
#
# p = PhoneBook()
# p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
# p.add_phone(PhoneNumber(21345678901, "Панда"))
# phones = p.get_phone_list()
# P.S. В программе требуется объявить только классы. На экран ничего выводить не нужно.


class PhoneBook:
    def __init__(self):
        self.lst_book = list()

    def add_phone(self, phone):
        self.lst_book.append(phone)

    def remove_phone(self, indx):
        self.lst_book.pop(indx)

    def get_phone_list(self):
        return self.lst_book


class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)
