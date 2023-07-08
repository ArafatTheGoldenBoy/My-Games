from Player import Player


def main():
    player1 = Player("Yasin", 28)
    player1.random_death()
    print(
        "Name:",
        player1.name,
        "\n",
        "Age:",
        player1.age,
        "\n",
        "Good Deeds:",
        player1.good_deeds,
        "\n",
        "Bad Deeds:",
        player1.bad_deeds,
        "\n",
        "Money:",
        player1.money,
    )
    player1.aging()
    player1.aging()
    print(player1.age)


main()
