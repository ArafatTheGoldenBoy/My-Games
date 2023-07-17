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
    all_life_history = []  # to find When character did shirk and repent in his lifetime
    special_case = [
        "Becouse you did the shirk but you didn't repent. According to islam Allah not forgive for your behavier. Final destination is Hell I geuss."
    ]

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
        random_age = randrange(self.age + 1, 63)
        self.time_line = random_age
        print("He will die at ", random_age)

    def daily_action(self):
        rd = randrange(-7, 7)
        if rd > 0:
            self.good_deeds += rd
            # ---- common situation for each timeline ----- #
            # ---- That means if anyone want to forgive then the sin become zero and----- #
            # ---- bad deeds counts as good deeds according 25-Surah Al-Furqan (The Criterion ) 70----- #
            # 6 becouse he did repent, Allah forgive him :)
            if rd == 6:
                self.good_deeds += -self.bad_deeds
                self.bad_deeds = 0
            self.good_life_history.append(self.good_action[rd])
            self.good_life_history.append(rd)
            self.all_life_history.append(self.good_action[rd])
        elif rd == 0:
            pass
        else:
            self.bad_deeds += rd
            self.bad_life_history.append(self.bad_action[-rd])
            self.bad_life_history.append(-rd)
            self.all_life_history.append(self.bad_action[-rd])
            # ---- End common situation ---- #

    def calculate_deeds(self):
        total_deeds = self.good_deeds + self.bad_deeds
        print("amol nama : ", total_deeds)
        # ---- Special Case ------#
        # ----- shirk calculation -----#
        lenght = len(self.all_life_history)
        position_of_shirk = -1
        position_of_repent = -1
        for x in range(lenght):
            if self.all_life_history[x] == "shirk":
                position_of_shirk = x
            elif self.all_life_history[x] == "repent":
                position_of_repent = x

        if self.all_life_history.pop() == "shirk":
            print(self.special_case[0])
        elif position_of_shirk > -1 and position_of_shirk > position_of_repent:
            print(self.special_case[0])
        # print("postion of shirk: ", position_of_shirk)
        # print("postion of repent: ", position_of_repent)
        # ---- Special Case End------#
        # ----- shirk calculation End-----#
        else:
            if total_deeds >= 0:
                print("Final destination: Paradise")
            else:
                print("Final destination: Hell")
