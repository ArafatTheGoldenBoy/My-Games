from Player import Player


def main():
    player1 = Player("Yasin", 28)
    # player1.random_death() [This function will need when I put some calculation with aging]
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
    print("Player's total lifetime is ", player1.time_line)
    # -------------Testing----------------#
    # ---- Player Start playing here------#
    for timeline in range(player1.time_line):
        player1.aging()
        if player1.age == player1.time_line:
            player1.is_alive = False
            break
    # ---------End Testing----------------#
    print(player1.age)
    print("Player is alive: ", player1.is_alive)


main()
