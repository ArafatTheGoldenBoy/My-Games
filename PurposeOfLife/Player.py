from random import randrange


class Player:
    name = "player"
    age = 13
    money = 1000
    good_deeds = 0
    bad_deeds = 0
    is_alive = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def aging(self):
        if self.is_alive == True:
            self.age += 1
        else:
            print("He died at age of ", self.age)

    def random_death(self):
        random_age = randrange(15, 60)
        print("He will die at ", random_age)
        if random_age == self.age:
            self.is_alive = False
