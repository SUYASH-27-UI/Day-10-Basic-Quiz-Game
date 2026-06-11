score = 0

print("Python Quiz")

answer = input("Q1. Python kis type ki language hai? ")

if answer.lower() == "programming":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("Q2. 2 + 2 = ? ")

if answer == "4":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Your Score:", score, "/ 2")
