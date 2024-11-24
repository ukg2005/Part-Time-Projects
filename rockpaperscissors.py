import random

options = ["rock","paper","scissors"]


def decide_winner(player,computer) :
    if player == computer:
        return 0
    elif player == "rock" and computer == "scissors" or \
        player == "scissors" and computer == "paper" or \
        player == "paper" and computer == "rock" :
        return 1
    else :
        return 2

def play_game():
    running = True
    while running :
        computer = random.choice(options)
        player = None
        player = input("Enter your choice(rock,paper,scissors):").lower()
        if player  not in options :
            print("Wrong choice(pick one from rock,paper,scissors)")
            continue
        else:
            print(f"Computer picked {computer} and You picked {player}")
            result = decide_winner(player,computer)
            if result == 0 :
                print("It's a draw")
            elif result == 1 :
                print("Congrats,You won")
            elif result == 2 :
                print("You lost")
        choice = input("Do you want to go again?(yes or no)").lower().strip()
        if choice != "yes" :
            print("Thanks for playing")
            running = False

if __name__ == "__main__" :
    play_game()