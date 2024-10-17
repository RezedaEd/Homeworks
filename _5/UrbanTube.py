import time
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                return print(f"Пользователь {nickname} уже существует.")
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошел в систему.")

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == user._User__hash_p(password):
                self.current_user = user
                return print(f'Пользователь {nickname} вошел в систему.')
        print('Неверный логин или пароль.')

    def log_out(self):
        self.current_user = None
        return 'Вы вышли из аккаунта.'

    def add(self, *videos):
        for video in videos:
            if self.videos == []:
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено.")
                continue
            for video_ in self.videos:
                if video_.title == video.title:
                    print(f"Видео '{video.title}' уже существует.")
                else:
                    self.videos.append(video)
                    print(f"Видео '{video.title}' добавлено.")
                    break

    def get_videos(self, word):
        result_ = []
        for video_ in self.videos:
            if word.casefold() in video_.title.casefold():
                result_.append(video_.title)
        return result_

    def watch_video(self, v_title):
        if self.current_user == None:
            return print('Войдите в аккаунт, чтобы смотреть видео.')
        for video_ in self.videos:
            if video_.title.casefold() == v_title.casefold():
                if video_.adult_mode and self.current_user.age < 18:
                    return print('Вам нет 18 лет. Пожалуйста, покиньте страницу.')
                print(f'Просмотр видео "{video_.title}":')
                while video_.time_now < video_.duration:
                    time.sleep(1)
                    video_.time_now += 1
                    print(f'{video_.time_now} ', end='')
                video_.time_now = 0
                return print('Конец видео.')
        print('Видео не найдено.')

    def current_user_(self):
        return print(self.current_user.nickname)

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age = age
        self.password = self.__hash_p(password)

    def __hash_p(self, password):
        return hash((self.nickname, password))


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 7)
v2 = Video('Для чего девушкам парень программист?', 3, adult_mode=True)

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
ur.current_user_()
ur.register('pikachu', 'F8098FM8fjm9jmi', 5)
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')