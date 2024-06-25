class User:
    def __init__(self, name, password, age):
        self.name = name
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = str()

    def log_in(self, login, password):
        for user in self.users:
            if login == user.name and hash(password) == user.password:
                self.current_user = login

    def register(self, nickname, password, age):
        if len(list(filter(lambda x: x.name == nickname, self.users))) > 0:
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(User(nickname, password, age))
            self.current_user = nickname

    def add(self, *args):
        for i in args:
            if len(list(filter(lambda x: x.title == i.title, self.videos))) == 0:
                self.videos.append(i)

    def get_videos(self, search):
        searches = []
        for video in self.videos:
            if search.lower() in video.title.lower():
                searches.append(video.title)
        return searches

    def watch_video(self, name_video):
        from time import sleep
        for video in self.videos:
            if video.title == name_video:
                if self.current_user:
                    if video.adult_mode == False or list(filter(lambda x: x.name == self.current_user, self.users))[0].age >= 18:
                        for sec in range(1, video.duration+1):
                            print(sec, end=' ')
                            sleep(1)
                        print('Конец видео')
                        break
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    print('Войдите в аккаунт, чтобы смотреть видео')



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



