# short version               (long version below)

menu = {"pizza":8.99,
        "apple":0.99,
        "book":1.49,
        "pen":0.99,
        "nachos":1.49,
        "bread":1.49
        }

cart = []
total = 0


print("------MENU------")
for key,value in menu.items():
    print(f"{key:10}:${value:.2f}")
print("-----------------")

while True :
    item = input("Enter item to cart(q to quit):").lower()
    if item == "q" :
        for item,quantity in cart:
            print(f"{quantity}x{item}:${menu.get(item)*quantity:.2f}")
        print(f"Total:${total:.2f}")
        print("Proceed to pay :)")
    elif item in menu:
        quantity = int(input("Enter the quantity of the item:"))
        cart.append((item,quantity))
        total += menu.get(item)*quantity
        print(f"{item.capitalize()} added to cart.",end = "\n")
        print(f"Current total:${total:.2f}")
    else:
        print(f"{item.capitalize()} not found.") 
    if item == "q":
        break


# long version

menu = {"pizza":8.99,
        "apple":0.99,
        "book":1.49,
        "pen":0.99,
        "nachos":1.49,
        "bread":1.49
        }

cart = []

def display_menu():
    print("------MENU------")
    for key,value in menu.items():
        print(f"{key:10}:${value:.2f}")
    print("-----------------")

def add_items():
    running = True
    while running :
        item = input("Enter item to add to cart(q to quit):")
        if item == "q" :
            print("Calculating total-----")
            calculate_total()
            running = False
        else:
            if item not in menu :
                print(f"{item} not found in the menu")
                continue
            else :
                try:
                    quantity = int(input("Enter the quantity of item:"))
                    cart.append((item,quantity))
                    print(f"{item} X {quantity} has been added to cart")
                except ValueError:
                    print("Invalid input,Enter integer")

def calculate_total(): 
    total = 0
    for item in cart:
        total += menu.get(item[0])*item[1]
    print(f"Total:${total:.2f}")

def view_cart():
    if not cart:
        print("Cart is empty")
        return
    print("------CART------")
    for item in cart:
        print(f"{item[0]:10} X {item[1]}:${menu.get(item[0])*item[1]:.2f}")
    print("----------------")

def main() :
    name = input("Enter your name:").capitalize()
    print(f"Welcome {name}")
    working = True
    while working:
        print("1.Display menu","2.Add to cart","3.Calculate total","4.View cart","5.Exit",sep = "\n")
        option = int(input("Enter your option:"))
        if option < 1 or option > 5:
            print("Invalid choice")
            continue
        match(option) :
            case 1:
                display_menu()
            case 2:
                add_items()
            case 3:
                calculate_total()
            case 4:
                view_cart()
            case 5:
                print("Thanks for shopping")
                working = False

if __name__ == "__main__":
    main()