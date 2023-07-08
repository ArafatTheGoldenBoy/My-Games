from random import randrange


class Player:
    name = "player"
    age = 13
    money = 1000
    good_deeds = 0
    bad_deeds = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
