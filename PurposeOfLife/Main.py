from Player import Player


def main():
    player1 = Player("Yasin", 29, "Male")
    player1.random_death()
    print("Player's total lifetime is ", player1.time_line)
    # -------------Testing----------------#
    # ---- Player Start playing here------#
    for timeline in range(player1.time_line):
        player1.daily_action()
        player1.aging()
        if player1.age == player1.time_line:
            player1.is_alive = False
            break
    # ---------End Testing----------------#
    print("Player is alive: ", player1.is_alive)
    player1.calculate_deeds()
    print("righteous deeds are : ", player1.good_life_history)
    print("Sins are : ", player1.bad_life_history)


main()
