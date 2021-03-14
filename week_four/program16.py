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


class Serie(Item):
    def __init__(self, name, genre, number_episode, length_episode):
        super().__init__(name, genre)
        self.number_episode = number_episode
        self.length_episode = length_episode

    def get_info(self):
        return f"{super().get_info()}, má celkem {self.number_episode} epizod a délka jedné epizody je {self.length_episode} minut."


first_movie = Movie("Pán Prstenů", "fantasy", 120)
print(first_movie.get_info())

first_serie = Serie("Přátelé", "rodinný", 200, 30)
print(first_serie.get_info())
