# Подвиг 6. Объявите класс AbstractClass, объекты которого нельзя было бы создавать.
# При выполнении команды:
#
# obj = AbstractClass()
# переменная obj должна ссылаться на строку с содержимым:
#
# "Ошибка: нельзя создавать объекты абстрактного класса"
#
# P.S. В программе объявить только класс, выводить на экран ничего не нужно.

class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return ("Ошибка: нельзя создавать объекты абстрактного класса")


obj = AbstractClass()
print(obj)


# Подвиг 7. Объявите класс SingletonFive, с помощью которого можно было бы создавать объекты командой:
#
# a = SingletonFive(<наименование>)
# Здесь <наименование> - это данные, которые сохраняются в локальном свойстве name созданного объекта.
#
# Этот класс должен формировать только первые пять объектов. Остальные (шестой, седьмой и т.д.)
# должны быть ссылкой на последний (пятый) созданный объект.
#
# Создайте первые десять объектов класса SingletonFive с помощью следующего фрагмента программы:
#
# objs = [SingletonFive(str(n)) for n in range(10)]
# P.S. В программе на экран ничего выводить не нужно.


class SingletonFive:
    _instance = None

    def __new__(cls, *args, **kwargs):
        for i in args:
            if int(i) < 4:
                cls._instance = super().__new__(cls)
                return super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
for i in objs:
    print(id(i))


# Подвиг 8. В программе объявлена переменная TYPE_OS и два следующих класса:
#
# TYPE_OS = 1 # 1 - Windows; 2 - Linux
#
# class DialogWindows:
#     name_class = "DialogWindows"
#
#
# class DialogLinux:
#     name_class = "DialogLinux"
# Необходимо объявить третий класс с именем Dialog, который бы создавал объекты командой:
#
# dlg = Dialog(<название>)
# Здесь <название> - это строка, которая сохраняется в локальном свойстве name объекта dlg.
#
# Класс Dialog должен создавать объекты класса DialogWindows, если переменная TYPE_OS = 1
# и объекты класса DialogLinux, если переменная TYPE_OS не равна 1. При этом, переменная TYPE_OS
# может меняться в последующих строчках программы. Имейте это в виду, при объявлении класса Dialog.
#
# P.S. В программе на экран ничего выводить не нужно. Только объявить класс Dialog.


TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        result = super().__new__(DialogWindows) if TYPE_OS == 1 else super().__new__(DialogLinux)
        for i in args:
            setattr(result, 'name', i)
        return result


dlg = Dialog('123')
print(type(dlg))
print(dlg.__dict__)


# Подвиг 9 (на повторение материала). Объявите класс Point для представления точек на плоскости.
# Создавать объекты этого класса предполагается командой:
#
# pt = Point(x, y)
# Здесь x, y - числовые координаты точки на плоскости (числа), то есть, в каждом объекте этого класса
# создаются локальные свойства x, y, которые хранят конкретные координаты точки.
#
# Необходимо в классе Point реализовать метод clone(self), который бы создавал новый объект класса Point
# как копию текущего объекта с локальными атрибутами x, y и соответствующими значениями.
#
# Создайте в программе объект pt класса Point и еще один объект pt_clone через вызов метода clone.
#
# P.S. В программе на экран ничего выводить не нужно.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        pt_clone = Point(self.x, self.y)
        return pt_clone


pt = Point(1, 2)
pt_clone = pt.clone()
print(id(pt), id(pt_clone))


# Подвиг 10 (на повторение материала). В программе предполагается реализовать парсер (обработчик) строки
# (string) в определенный выходной формат. Для этого объявлен следующий класс:
#
# class Loader:
#     def parse_format(self, string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
# И предполагается его использовать следующим образом:
#
# ld = Loader()
# res = ld.parse_format("4, 5, -6.5", Factory())
# На выходе (в переменной res) ожидается получить список из набора вещественных чисел. Например,
# для заданной строки, должно получиться:
#
# [4.0, 5.0, -6.5]
#
# Для реализации этой идеи необходимо вначале программы прописать класс Factory с двумя методами:
#
# build_sequence(self) - для создания начального пустого списка (метод должен возвращать пустой список);
# build_number(self, string) - для преобразования переданной в метод строки (string) в вещественное значение
# (метод должен возвращать полученное вещественное число).
#
# Объявите класс с именем Factory, чтобы получать на выходе искомый результат.
#
# P.S. В программе на экран ничего выводить не нужно.


class Factory:
    def build_sequence(self):
        lst = []
        return lst

    def build_number(self, string):
        return float(string)


class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
ld = Loader()
s = input()
res = ld.parse_format(s, Factory())
print(res)
