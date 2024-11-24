
import random

words = [
    "apple", "banana", "grape", "orange", "strawberry",
    "elephant", "tiger", "giraffe", "dolphin", "kangaroo",
    "mountain", "river", "ocean", "valley", "desert",
    "python", "laptop", "keyboard", "monitor", "software",
    "spaceship", "planet", "galaxy", "asteroid", "comet",
    "umbrella", "raincoat", "weather", "sunshine", "cloud",
    "triangle", "circle", "hexagon", "octagon", "square"
]#you can use this list or create a script with larger set and import it

hangman_art = {
    0 : ("   ",
         "   ",
         "   "),
    1 : (" o ",
         "   ",
         "   "),
    2 : (" o ",
         " | ",
         "   "),
    3 : (" o ",
         "/| ",
         "   "),
    4 : (" o ",
         "/|\\",
         "   "),
    5 : (" o ",
         "/|\\",
         "/  "),
    6 : (" o ",
         "/|\\",
         "/ \\")
}

def display_man(wrong_guesses):
    if wrong_guesses in range(7):
        for line in hangman_art[wrong_guesses]:
            print(line)
    else:
        return 0

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def play_game():
    answer = random.choice(words)
    is_running = True
    wrong_guesses = 0
    hint = ["_"]*len(answer)
    total_guesses = 0
    guesses = []

    while is_running:

        display_hint(hint)

        guess = input("Enter a letter to guess:").lower().strip()
        
        if guess not in guesses:
            guesses.append(guess)
            total_guesses += 1
        else:
            print(f"'{guess}' is already guessed")
            continue

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess           
        if guess not in answer:
            wrong_guesses += 1
        
        print("************")
        display_man(wrong_guesses)
        print("************")

        if '_' not in hint:
            print()
            print("Congrats,You got it right")
            print(f"It took you {guesses} attempts")
            print()
            break

        if wrong_guesses >= 6:
            print()
            print("You ran out of attempts")
            print(f"Answer:{answer}")
            print()
            break

def main ():
    print("Welcome to hangman")
    while True:
        play_game()
        choice = input("Do you want to go again?(Y/N)").strip().upper()
        if choice != 'Y':
            print("Thanks for playing")
            break

if __name__ == '__main__':
    main()