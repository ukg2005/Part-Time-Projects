
def show_balance(balance):
    print(f"Your account balance:${balance:.2f}")

def withdraw(balance):
    amount = float(input("Enter amount to withdraw:"))
    try:
        if amount > balance:
            print("Insufficient balance")
        elif amount < 0:
            print("**************")
            print("Invalid amount")
            print("**************")
        else :
            balance -= amount
            print(f"${amount:.2f} withdrawn")
            print(f"Account balance:${balance:.2f}")
    except ValueError:
        print("Enter valid amount:")
    return balance

def deposit(balance):
    amount = float(input("Enter amount to deposit:"))
    try:
        if amount < 0:
            print("**************")
            print("Invalid amount")
            print("**************")
        else:
            balance += amount
            print(f"${amount:.2f} deposited")
            print(f"Account balance:${balance:.2f}")
    except ValueError:
        print("Enter valid amount:")
    return balance

def main () :
    balance = 0
    is_running = True
    name = input("Enter your name:").capitalize()
    print(f"Welcome {name}")
    while is_running:
        print("***************")
        print("1.View balance","2.Withdraw","3.Deposit","4.Exit",sep = "\n")
        print("***************")
        choice = int(input("Enter your choice(1 to 4):"))
        if choice < 0 or choice > 4:
            print("*************")
            print("Wrong input")
            print("*************")
            continue
        match (choice):
            case 1:
                show_balance(balance)
            case 2:
                balance = withdraw(balance)
            case 3:
                balance = deposit(balance)
            case 4:
                print("Exiting....")
                is_running = False

if __name__ == "__main__":
    main()