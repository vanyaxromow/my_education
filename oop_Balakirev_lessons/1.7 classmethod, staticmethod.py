# Подвиг 6. В программе предполагается реализовать парсер (обработчик) строки с данными string в
# определенный выходной формат. Для этого объявлен следующий класс:
#
# class Loader:
#     @staticmethod
#     def parse_format(string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
# И предполагается его использовать следующим образом:
#
# res = Loader.parse_format("4, 5, -6", Factory)
# На выходе (в переменной res) ожидается получать список из набора целых чисел. Например, для заданной строки,
# должно получиться:
#
# [4, 5, -6]
#
# Для реализации этой идеи необходимо вначале программы прописать класс Factory с двумя статическими методами:
#
# build_sequence() - для создания пустого списка (метод возвращает пустой список);
# build_number(string) - для преобразования строки (string) в целое число (метод возвращает полученное
# целочисленное значение).
#
# Объявите класс с именем Factory, чтобы получать на выходе искомый результат.
#
# P.S. В программе на экран ничего выводить не нужно.


class Factory:
    @staticmethod
    def build_sequence():
        return []

    @staticmethod
    def build_number(string):
        return int(string)


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
res = Loader.parse_format("1, 2, 3, -5, 10", Factory)


# Подвиг 7. В программе объявлен следующий класс для работы с формами ввода логин/пароль:
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
# Который предполагается использовать следующим образом:
#
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()
# Необходимо прописать классы TextInput и PasswordInput, объекты которых формируются командами:
#
# login = TextInput(name, size)
# psw = PasswordInput(name, size)
# В каждом объекте этих классов должны быть следующие локальные свойства:
#
# name - название для поля (сохраняет передаваемое имя, например, "Логин" или "Пароль");
# size - размер поля ввода (целое число, по умолчанию 10).
#
# Также классы TextInput и PasswordInput должны иметь метод:
#
# get_html(self) - возвращает сформированную HTML-строку в формате (1-я строка для класса TextInput ;
# 2-я - для класса PasswordInput):
#
# <p class='login'><имя поля>: <input type='text' size=<размер поля> />
# <p class='password'><имя поля>: <input type='text' size=<размер поля> />
#
# Например, для поля login:
#
# <p class='login'>Логин: <input type='text' size=10 />
#
# Также классы TextInput и PasswordInput должны иметь метод класса (@classmethod):
#
# check_name(cls, name) - для проверки корректности переданного имя поля (следует вызывать в инициализаторе)
# по следующим критериям:
#
# - длина имени не менее 3 символов и не более 50;
# - в именах могут использоваться только символы русского, английского алфавитов, цифры и пробелы
#
# Если проверка не проходит, то генерировать исключение командой:
#
# raise ValueError("некорректное поле name")
# Для проверки допустимых символов в каждом классе должен быть прописан атрибут CHARS_CORRECT:
#
# CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
# CHARS_CORRECT = CHARS + CHARS.upper() + digits
# По заданию нужно объявить только классы TextInput и PasswordInput с соответствующим функционалом. Более ничего.
#
# P. S. В данном задании получится дублирование кода в классах TextInput и PasswordInput. На данном этапе - это
# нормально.


from string import ascii_lowercase, digits


# здесь объявляйте классы TextInput и PasswordInput
class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    PASS = 'login'

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='{self.PASS}'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        if 3 <= len(name) <= 50 and set(name) < set(cls.CHARS_CORRECT):
            return True
        else:
            raise ValueError("некорректное поле name")


class PasswordInput(TextInput):
    PASS = 'password'


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()


# Подвиг 8. Объявите класс CardCheck для проверки корректности информации на пластиковых картах.
# Этот класс должен иметь следующие методы:
#
# check_card_number(number) - проверяет строку с номером карты и возвращает булево значение True,
# если номер в верном формате и False - в противном случае. Формат номера следующий: XXXX-XXXX-XXXX-XXXX,
# где X - любая цифра (от 0 до 9).
# check_name(name) - проверяет строку name с именем пользователя карты. Возвращает булево значение True,
# если имя записано верно и False - в противном случае.
#
# Формат имени: два слова (имя и фамилия) через пробел, записанные заглавными латинскими символами и цифрами.
# Например, SERGEI BALAKIREV.
#
# Предполагается использовать класс CardCheck следующим образом (эти строчки в программе не писать):
#
# is_number = CardCheck.check_card_number("1234-5678-9012-0000")
# is_name = CardCheck.check_name("SERGEI BALAKIREV")
# Для проверки допустимых символов в классе должен быть прописан атрибут:
#
# CHARS_FOR_NAME = ascii_lowercase.upper() + digits
# Подумайте, как правильнее объявить методы check_card_number и check_name
# (декораторами @classmethod и @staticmethod).
#
# P.S. В программе только объявить класс. На экран ничего выводить не нужно.


from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @classmethod
    def check_card_number(cls, number):
        example = 'XXXX-XXXX-XXXX-XXXX'
        if len(example) == len(number):
            return all(number[i] in digits if j == "X" else number[i] == j for i, j in enumerate('XXXX-XXXX-XXXX-XXXX'))
        return False

    @staticmethod
    def check_name(name):
        return all(x in ascii_lowercase.upper() + ' ' if len(name.split(sep=' ')) == 2 else False for x in name)

#
# Подвиг 9. Объявите в программе класс Video с двумя методами:
#
# create(self, name) - для задания имени name текущего видео (метод сохраняет имя name в локальном атрибуте
# name объекта класса Video);
# play(self) - для воспроизведения видео (метод выводит на экран строку "воспроизведение видео <name>").
#
# Объявите еще один класс с именем YouTube, в котором объявите два метода (с декоратором @classmethod):
#
# add_video(cls, video) - для добавления нового видео (метод помещает объект video класса Video в список);
# play(cls, video_indx) - для проигрывания видео из списка по указанному индексу (индексация с нуля).
#
# (здесь cls - ссылка на класс YouTube). И список (тоже внутри класса YouTube):
#
# videos - для хранения добавленных объектов класса Video (изначально список пуст).
#
# Метод play() класса YouTube должен обращаться к объекту класса Video по индексу списка videos и, затем,
# вызывать метод play() класса Video.
#
# Методы add_video и play вызывайте напрямую из класса YouTube. Создавать экземпляр этого класса не нужно.
#
# Создайте два объекта v1 и v2 класса Video, затем, через метод create() передайте им имена "Python" и
# "Python ООП". После этого с помощью метода add_video класса YouTube, добавьте в него эти два видео и
# воспроизведите (с помощью метода play класса YouTube) сначала первое, а затем, второе видео.


class Video:
    def create(self, name):
        self.name = name

    def play(self):
        print(f"воспроизведение видео {self.name}")


class YouTube:
    videos = []

    @classmethod
    def add_video(cls, video):
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):
        cls.videos[video_indx].play()


v1 = Video()
v2 = Video()
v1.create("Python")
v2.create("Python ООП")
YouTube.add_video(v1)
YouTube.add_video(v2)
YouTube.play(0)
YouTube.play(1)


# Подвиг 10 (на повторение). Объявите класс AppStore - интернет-магазин приложений для устройств под iOS.
# В этом классе должны быть реализованы следующие методы:
#
# add_application(self, app) - добавление нового приложения app в магазин;
# remove_application(self, app) - удаление приложения app из магазина;
# block_application(self, app) - блокировка приложения app (устанавливает локальное свойство blocked объекта app
# в значение True);
# total_apps(self) - возвращает общее число приложений в магазине.
#
# Класс AppStore предполагается использовать следующим образом (эти строчки в программе не писать):
#
# store = AppStore()
# app_youtube = Application("Youtube")
# store.add_application(app_youtube)
# store.remove_application(app_youtube)
# Здесь Application - класс, описывающий добавляемое приложение с указанным именем. Каждый объект класса
# Application должен содержать локальные свойства:
#
# name - наименование приложения (строка);
# blocked - булево значение (True - приложение заблокировано; False - не заблокировано, изначально False).
#
# Как хранить список приложений в объектах класса AppStore решите сами.
#
# P.S. В программе нужно только объявить классы с указанным функционалом.


class AppStore:
    APPLICATIONS = []

    def add_application(self, app):
        self.APPLICATIONS.append(app)

    def remove_application(self, app):
        for i in self.APPLICATIONS:
            if i is app:
                self.APPLICATIONS.remove(app)

    def block_application(self, app):
        self.app.blocked = True

    def total_apps(self):
        return len(self.APPLICATIONS)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked


a = AppStore()
a.add_application(a)
print(a.APPLICATIONS)
a.remove_application(a)
print(a.APPLICATIONS)


# Подвиг 11 (на повторение). Объявите класс для мессенджера с именем Viber. В этом классе должны быть
# следующие методы:
#
# add_message(msg) - добавление нового сообщения в список сообщений;
# remove_message(msg) - удаление сообщения из списка;
# set_like(msg) - поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like объекта msg:
# если лайка нет то он ставится, если уже есть, то убирается);
# show_last_message(число) - отображение последних сообщений;
# total_messages() - возвращает общее число сообщений.
#
# Эти методы предполагается использовать следующим образом (эти строчки в программе не писать):
#
# msg = Message("Всем привет!")
# Viber.add_message(msg)
# Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.set_like(msg)
# Viber.remove_message(msg)
# Класс Message (необходимо также объявить) позволяет создавать объекты-сообщения со следующим набором
# локальных свойств:
#
# text - текст сообщения (строка);
# fl_like - поставлен или не поставлен лайк у сообщения (булево значение True - если лайк есть и False - в
# противном случае, изначально False);
#
# P.S. Как хранить список сообщений, решите самостоятельно.


class Viber:
    dict_message = {}

    @classmethod
    def add_message(cls, msg):
        cls.dict_message[msg] = msg.text

    @classmethod
    def remove_message(cls, msg):
        del cls.dict_message[msg]

    @classmethod
    def set_like(cls, msg):
        msg.fl_like = not msg.fl_like

    @classmethod
    def show_last_message(cls, x: int):
        print(list(cls.dict_message.values())[-x::])

    @classmethod
    def total_messages(cls):
        return len(cls.dict_message)


class Message:
    def __init__(self, text):
        self.text = text
        self.fl_like = False


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
# Viber.remove_message(msg)
print(Viber.dict_message, Viber.total_messages())
print(Viber.show_last_message(1))


# Время первого испытания. Представьте, что вы получили задание от заказчика. Вас просят реализовать простую
# имитацию локальной сети, состоящую из набора серверов, соединенных между собой через роутер.
#
# Каждый сервер может отправлять пакет любому другому серверу сети. Для этого у каждого есть свой уникальный IP-адрес.
# Для простоты - это просто целое (натуральное) число от 1 и до N, где N - общее число серверов. Алгоритм следующий.
# Предположим, сервер с IP = 2 собирается отправить пакет информации серверу с IP = 3. Для этого, он сначала
# отправляет пакет роутеру, а уже тот, смотрит на IP-адрес и пересылает пакет нужному узлу (серверу).
#
# Для реализации этой схемы программе предлагается объявить три класса:
#
# Server - для описания работы серверов в сети;
# Router - для описания работы роутеров в сети (в данной задаче полагается один роутер);
# Data - для описания пакета информации.
#
# Серверы будут создаваться командой:
#
# sv = Server()
# При этом, уникальный IP-адрес каждого сервера должен формироваться автоматически при создании нового экземпляра
# класса Server.
#
# Далее, роутер должен создаваться аналогичной командой:
#
# router = Router()
# А, пакеты данных, командой:
#
# data = Data(строка с данными, IP-адрес назначения)
# Для формирования и функционирования локальной сети, в классе Router должны быть реализованы следующие методы:
#
# link(server) - для присоединения сервера server (объекта класса Server) к роутеру (для простоты, каждый сервер
# соединен только с одним роутером);
# unlink(server) - для отсоединения сервера server (объекта класса Server) от роутера;
# send_data() - для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам
# (после отправки буфер должен очищаться).
#
# И одно обязательное локальное свойство (могут быть и другие свойства):
#
# buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
#
# Класс Server должен содержать свой набор методов:
#
# send_data(data) - для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом получателя
# (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);
# get_data() - возвращает список принятых пакетов (если ничего принято не было, то возвращается пустой список)
# и очищает входной буфер;
# get_ip() - возвращает свой IP-адрес.
#
# Соответственно в объектах класса Server должны быть локальные свойства:
#
# buffer - список принятых пакетов (объекты класса Data, изначально пустой);
# ip - IP-адрес текущего сервера.
#
# Наконец, объекты класса Data должны содержать два следующих локальных свойства:
#
# data - передаваемые данные (строка);
# ip - IP-адрес назначения.
#
# Пример использования этих классов (эти строчки в программе писать не нужно):
#
# router = Router()
# sv_from = Server()
# sv_from2 = Server()
# router.link(sv_from)
# router.link(sv_from2)
# router.link(Server())
# router.link(Server())
# sv_to = Server()
# router.link(sv_to)
# sv_from.send_data(Data("Hello", sv_to.get_ip()))
# sv_from2.send_data(Data("Hello", sv_to.get_ip()))
# sv_to.send_data(Data("Hi", sv_from.get_ip()))
# router.send_data()
# msg_lst_from = sv_from.get_data()
# msg_lst_to = sv_to.get_data()
# Ваша задача реализовать классы Router, Server и Data в соответствии с приведенным техническим заданием (ТЗ).
# Что-либо выводить на экран не нужно.


class Router:
    def __init__(self):
        self.buffer = []
        self.routing_table = []

    def link(self, server):
        self.routing_table.append(server)
        server.route = self

    def unlink(self, server):
        self.routing_table.remove(server)

    def send_data(self):
        for packet in self.buffer:
            for server in self.routing_table:
                if packet.send_to_ip == server.ip:
                    server.buffer.append(packet)

        self.buffer.clear()


class Server:
    def __init__(self):
        self.ip = id(self)
        self.buffer = []
        self.route = None

    def send_data(self, data):
        if self.route:
            self.route.buffer.append(data)

    def get_data(self):
        res = self.buffer[:]
        self.buffer.clear()
        return res

    def get_ip(self):
        return self.ip


class Data:
    def __init__(self, str_data, send_to_ip):
        self.data = str_data
        self.send_to_ip = send_to_ip


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
