import random

low_limit = 1
high_limit = 100
number = random.randint(low_limit, high_limit)
print("Let's start the Python Number Guessing Game")
print(f"Guess the number between {low_limit} and {high_limit}:")
guesses = 1
while True:
    guess = input("Enter your guess:")
    if guess.isdigit():
        guess = int(guess)
        if guess > high_limit or guess < low_limit:
            print(f"{guess} is out of range,Try again")
            print(f"Enter a number between {low_limit} and {high_limit}")
        elif guess == number :
            print("Congrats, you got it right")
            if guesses == 1:
                print("It took you only one try!")
            else :
                print(f"It took you {guesses} tries")
            break
        else:
            if guess > number :
                print("You're guess is high!Try something lower")
            elif guess < number :
                print("You're guess is low!Try something higher")
        guesses += 1
    else :
        print("Wrong input")
        print(f"Enter a number between {low_limit} and {high_limit}")