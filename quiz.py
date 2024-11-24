question = ("What is the capital of india?",
            "How many months are in a year?",
            "What is the symbol of gold?")

options = (("A.new delhi","B.mumbai","C.hyderabad","D.paris"),
           ("A.14","B.12","C.9","D.10"),
           ("A.Ag","B.g","C.Au","D.Pt"))

answers = ("A","B","C")

guess = []

print("-----Questions-----")
for q in range(3):
    print(question[q])
    for option in options[q]:
        print(option)
    answer = input("Enter your answer:").upper()
    guess.append(answer)

count = 0

for g in range(3):
    if guess[g] == answers[g]:
        count += 1
print(f"You got {count} questions right")