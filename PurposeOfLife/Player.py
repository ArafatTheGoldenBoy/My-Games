from random import randrange


class Player:
    name = "player"
    age = 13
    money = 1000
    good_deeds = 0
    bad_deeds = 0
    is_alive = True
    time_line = 60

    def __init__(self, name, age):
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
        rd = randrange(-100, 100)
        if rd > 0:
            self.good_deeds += 1
        else:
            self.bad_deeds += 1

    def calculate_deeds(self):
        total_deeds = self.good_deeds - self.bad_deeds
        print("amol nama : ", total_deeds)
        if total_deeds > 0:
            print("Final destination: Paradise")
        else:
            print("Final destination: Hell")
