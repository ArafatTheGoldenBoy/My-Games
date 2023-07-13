from random import randrange


class Player:
    name = "player"
    age = 13
    gender = "none"
    good_deeds = 0
    bad_deeds = 0
    is_alive = True
    time_line = 60
    good_action = [
        "zero",
        "charity",
        "prayer for others",
        "haz",
        "zakat",
        "salat",
        "repent",
        "tawhid",
    ]
    bad_action = ["zero", "greed", "envy", "lust", "wrath", "sloth", "murder", "shirk"]
    good_life_history = []
    bad_life_history = []

    def __init__(self, name, age, gender):
        self.gender = gender
        self.name = name
        self.age = age

    def aging(self):
        if self.is_alive == True:
            self.age += 1
        else:
            print("He died at age of ", self.age)

    def random_death(self):
        random_age = randrange(self.age + 1, 60)
        self.time_line = random_age
        print("He will die at ", random_age)

    def daily_action(self):
        rd = randrange(-7, 7)
        if rd > 0:
            self.good_deeds += rd
            self.good_life_history.append(self.good_action[rd])
        elif rd == 0:
            pass
        else:
            self.bad_deeds += rd
            self.bad_life_history.append(self.bad_action[rd])
            # ---- common situation for each timeline ----- #
            # ---- That means if anyone want to forgive then the sin become zero and----- #
            # ---- bad deeds counts as good deeds according 25-Surah Al-Furqan (The Criterion ) 70----- #
            repent = randrange(0, 20)
            # 7 becouse his repent, Allah forgive him :)
            if repent == 7:
                self.good_deeds += self.bad_deeds
                self.bad_deeds = 0
            # ---- End common situation ---- #

    def calculate_deeds(self):
        total_deeds = self.good_deeds - self.bad_deeds
        print("amol nama : ", total_deeds)
        if total_deeds >= 0:
            print("Final destination: Paradise")
        else:
            print("Final destination: Hell")
