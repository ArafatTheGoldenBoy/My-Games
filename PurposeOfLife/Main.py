from Player import Player


def main():
    player1 = Player("Yasin", 28)

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


main()
