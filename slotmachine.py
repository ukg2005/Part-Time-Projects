import random

def spin_row():
    options = ['🍒','🔔','🍉','⭐','🍋']
    return [random.choice(options) for _ in range(3)] #list comprehension

def print_row(row):
    print("********")
    print("|".join(row))
    print("********")

def calculate_payout(row,bet):
    # if row[0] == row[1] == row[2]:
    #     if row[0] == '🍒':
    #         return bet*2
    #     elif row[0] == '🔔':
    #         return bet*3
    #     elif row[0] == '🍉':
    #         return bet*5
    #     elif row[0] == '⭐':
    #         return bet*10
    #     elif row[0] == '🍋':
    #         return bet*20
    # return 0
    symbol_payout = {'🍒':2,'🔔':3,'🍉':5,'⭐':10,'🍋':20} #dictionary
    if row[0] == row[1] == row[2]:
        return bet * symbol_payout.get(row[0],0)
    return 0

def main():
    balance = 100

    print("******************************")
    print("Welcome to python slot machine")
    print("Symbols :🍒 🔔 🍉 ⭐ 🍋")
    print("******************************")

    while balance > 0:
        print(f"Current balance:${balance:.2f}")
        bet = input("Enter your bet:")
        if not bet.isdigit():
            print("Invalid bet")
            continue
        bet = int (bet)
        if bet <= 0:
            print("Bet should be greater than 0")
            continue
        if balance < bet:
            print("Insufficient balance")
            continue
        balance -= bet
        row = spin_row()
        print_row(row)
        payout = calculate_payout(row,bet)
        if payout > 0:
            print((f"Congrats,You won ${payout:.2f}"))
            balance += payout
            print(f"Balance:${balance:.2f}")
        else:
            print("You lost")
        choice = input("Do you want to go again(Y/N):").strip().upper()
        if choice == 'Y':
            continue
        else :
            print("Thanks for playing")
            print(f"Your final balance:${balance:.2f}")
            break

if __name__ == '__main__':
    main()