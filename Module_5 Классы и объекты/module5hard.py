import time


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and hash(password) == user.password:
                self.current_user = user
                break
        else:
            print("Такого пользователя не существует")

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f"Пользователь {nickname} уже существует")
                break
        else:
            user = User(nickname, hash(password), age)
            self.users.append(user)
            self.current_user = user

    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта")

    def add(self, *videos):
        new_videos = list(videos)
        for video in new_videos:
            if video.title not in [saved_video.title for saved_video in self.videos]:
                self.videos.append(video)

    def get_videos(self, search_word):
        search_videos = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                search_videos.append(video.title)
        return search_videos

    def watch_video(self, title):
        for video in self.videos:
            if video.title == title:
                if self.current_user:
                    if not video.adult_mode or video.adult_mode and self.current_user.age >= 18:
                        for sec in range(video.time_now+1, video.duration+1):
                            time.sleep(1)
                            print(sec, end=" ")
                        print("Конец видео")
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    print("Войдите в аккаунт, чтобы смотреть видео")
                break



class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
