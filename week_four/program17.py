class Item:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def get_info(self):
        print(f"{self.name} je žánru {self.genre} ")


class Movie(Item):
    def __init__(self, name, genre, length):
        super().__init__(name, genre)
        self.length = length

    def get_info(self):
        return f"{super().get_info()} a trvá {self.length} minut."

    def get_length(self):
        return f"Délka filmu je celkem {self.lengthe} minut."


class Serie(Item):
    def __init__(self, name, genre, number_episode, length_episode):
        super().__init__(name, genre)
        self.number_episode = number_episode
        self.length_episode = length_episode
        self.length_final = self.length_episode * self.number_episode

    def get_info(self):
        return f"{super().get_info()}, má celkem {self.number_episode} epizod a délka jedné epizody je {self.length_episode} minut."

    def get_length(self):
        return f"Délka filmu je celkem {self.length_final/60} hodin."


class User:
    def __init__(self, user_name):
        self.user_name = user_name
        self.watching_time = 0
        self.watched_items = {}

    def watched(self, time):
        self.watched_items[time.name] = int(time.length_final)
        return f"Uživatel {self.user_name} již zhlédnul {self.watched_items}."

    def add_watched(self, time):
        self.watching_time += time.length_final
        return f"Uživatel celkem zhlédnul {self.watching_time / 60} hodin mediálního obsahu."

    def final_length(self):
        for k, v in self.watched_items.items():
            self.watching_time += v
        return f"Uživatel již zhlédnul {self.watching_time / 60} hodin mediálního obsahu."


first_movie = Movie("Pán Prstenů", "fantasy", 120)
print(first_movie.get_info())

first_serie = Serie("Přátelé", "rodinný", 200, 30)
print(first_serie.get_info())

test_user = User("Karel Novák")
print(test_user.add_watched(first_serie))
print(test_user.watched(first_serie))
print(test_user.final_length())
