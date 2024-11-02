class User:
    '''
    Класс пользователя, содержащий логин и пароль
    '''
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password_confirm == password:
            self.password = password


class Darabase:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

if __name__ == "__main__":
    datebase = Darabase()
    while True:
        choice = input("Здравствуйте! Выберете действие:\n1 - Войти\n2 - Зарегистрироваться\n")
        if choice == '2':
            user = User(input("Введите логин: "), password := input("Введите пароль: "),
                        password2 := input("Повторите пароль: "))
            if password == password2:
                datebase.add_user(user.username, user.password)
                print("Вы успешно зарегистрированы!")
            else:
                print("Пароли не совпадают")
                continue
        elif choice == '1':
            log_username = input("Введите логин: ")
            log_password = input("Введите пароль: ")
            if log_username in datebase.data:
                if datebase.data[log_username] == log_password:
                    print("Вы успешно вошли!")
                    break
                else:
                    print("Неверный пароль")
            else:
                print("Такого пользователя не существует")