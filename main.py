from random import randint


def snake_ladder():
    players = {
        "Player 1": 0,
        "Player 2": 0,
        "Player 3": 0
    }
    dimension = int(input(f"Please enter board dimension:"))
    last_position = dimension * dimension

    position_p1 = []
    position_p2 = []
    position_p3 = []

    roll_p1 = []
    roll_p2 = []
    roll_p3 = []

    while True:

        for player in players:
            roll = randint(1, 6)
            if player == "Player 1":
                roll_p1.append(roll)
            elif player == "Player 2":
                roll_p2.append(roll)
            elif player == "Player 3":
                roll_p3.append(roll)


            new_position = players[player] + roll

            if new_position > last_position:
                print(f"{player} Invalid dice roll")
            else:
                players[player] = new_position
                if player == "Player 1":
                    position_p1.append(new_position)
                elif player == "Player 2":
                    position_p2.append(new_position)
                elif player == "Player 3":
                    position_p3.append(new_position)

            for key, value in players.items():
                if players[player] == players[key] and players[key] > 0 and player != key:
                    print(f"{key} have been crossed by {player}")
                    print(f"{key} position resets to 0")
                    players[key] = 0

            if players[player] == last_position:
                print(f"{player} won the game!!!")
                print(f"Player 1 position history: {position_p1} and roll history : {roll_p1}")
                print(f"Player 2 position history: {position_p2} and roll history : {roll_p2}")
                print(f"Player 3 position history: {position_p3} and roll history : {roll_p3}")
                return


snake_ladder()
