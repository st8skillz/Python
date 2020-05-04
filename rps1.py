# Spencer Goldwin
#cit 299
#April 2020

player1_wins = 0
player2_wins = 0

def User1_Choose_Option():
    user1_choice = input("Player 1 choose Rock, Paper or Scissors: ")
    if user1_choice in ["Rock", "rock", "r", "R"]:
        user1_choice = "r"
    elif user1_choice in ["Paper", "paper", "p", "P"]:
        user1_choice = "p"
    elif user1_choice in ["Scissors", "scissors", "s", "S"]:
        user1_choice = "s"
    else:
        print("I don't understand, try again.")
        User1_Choose_Option()
    return user1_choice

def User2_Choose_Option():
    user2_choice = input("Player 2 hoose Rock, Paper or Scissors: ")
    if user2_choice in ["Rock", "rock", "r", "R"]:
        user2_choice = "r"
    elif user2_choice in ["Paper", "paper", "p", "P"]:
        user2_choice = "p"
    elif user2_choice in ["Scissors", "scissors", "s", "S"]:
        user2_choice = "s"
    else:
        print("I don't understand, try again.")
        User2_Choose_Option()
    return user2_choice


while True:
    print("")

    user1_choice = User1_Choose_Option()
    user2_choice = User2_Choose_Option()

    print("")

    if user1_choice == "r":
        if user2_choice == "r":
            print("Player 1 chose rock. Player 2 chose rock You tie")

        elif user2_choice == "p":
            print("Player 1 chose rock. Player 2 chose paper. Player 2 wins.")
            player2_wins += 1

        elif user2_choice == "s":
            print("Player 1 chose rock. Player 2 chose scissors. Player 1 wins.")
            player1_wins += 1

    elif user1_choice == "p":
        if user2_choice == "r":
            print("Player 1 chose paper. Player 2 chose rock. Player 1 wins.")
            player1_wins += 1

        elif user2_choice == "p":
            print("Player 1 chose paper. Player 2  chose paper. You tied.")


        elif user2_choice == "s":
            print("Player 1 chose paper. Player 2 chose scissors Player 2 wins.")
            player2_wins += 1

    elif user1_choice == "s":
        if user2_choice == "r":
            print("Player 1 chose scissors. Player 2 chose rock. Player 2 wins.")
            player2_wins += 1

        elif user2_choice == "p":
            print("Player 1 chose scissors. Player 2 chose paper. Player 1 wins.")
            player1_wins += 1

        elif user2_choice == "s":
            print("Player 1 chose scissors. Player 2 chose scissors. You tie")

    print("")
    print("Player 1 wins: " + str(player1_wins))
    print("Player 2 wins: " + str(player2_wins))
    print("")

    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break
