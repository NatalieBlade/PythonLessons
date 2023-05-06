class User():
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.count = 0

    def log_in(self):
        """Залогиниться"""
        log_in = input("Введите логин: ")
        pass_word = input("Введите пароль: ")
        if log_in == self.login and pass_word == self.password:
            print("Вы успешно залогинились")
            self.count = self.count + 1
            print(self.count)
        else:
            print("Проверьте введенные данные")

    def log_out(self):
        """Разлогиниться"""
        print("Хотите выйти?")
        x = input("Введите да или нет: ")
        if x == "да":
            print("Вы вышли из аккаунта")
        elif x == "нет":
            print("Вы все еще с нами!")
        else:
            print("Введите да или нет: ")

    def login_count(self, times):
        """Считаем количество заходов"""
        if times >= 1:
            self.count += times
            print(self.count)
        else:
            print("Войдите в аккаунт")

class Admin(User):
    def __init__(self, login, password, privil):
        super().__init__(login, password)
        self.privil = privil

    def priv(self):
        print("Администратор может: \n1) Просматривать ваш аккаунт \n2) Присать вам письма \n3) Звонить вам по ночам")

adm = Admin("sobolev", "987654321", "Повелитель аккаунтов")
adm.priv()
# user = User(2"korolev", "13456789")
#
# user.log_in()
# user.log_out()
# user.count = 2
# user.login_count(2)