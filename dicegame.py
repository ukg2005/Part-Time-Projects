import random

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘

dice_art = {
    1 : ("┌─────────┐",
         "│         │",
         "│    ●    │",
         "│         │",
         "└─────────┘"),
    2 : ("┌─────────┐",
         "│  ●      │",
         "│         │",
         "│      ●  │",
         "└─────────┘"),
    3 : ("┌─────────┐",
         "│ ●       │",
         "│    ●    │",
         "│       ● │",
         "└─────────┘"),
    4 : ("┌─────────┐",
         "│ ●     ● │",
         "│         │",
         "│ ●     ● │",
         "└─────────┘"),
    5 : ("┌─────────┐",
         "│ ●     ● │",
         "│    ●    │",
         "│ ●     ● │",
         "└─────────┘"),
    6 : ("┌─────────┐",
         "│ ●  ●  ● │",
         "│         │",
         "│ ●  ●  ● │",
         "└─────────┘")
}

dice = []
total = 0

no_of_dice = int(input("Enter the number of tries:"))

for die in range(no_of_dice) :
   dice.append(random.randint(1, 6))

print(f"Dice rolls:",dice)

for line in range(5):
   for die in dice:
      print(dice_art.get(die)[line],end = "")
   print()

for item in dice:
   total += item
print(f"Total:{total}")