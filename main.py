import random
import string
from counting import count_bulls, count_cows


while len(set((ANSWER := "".join(random.choices(string.digits, k=4))))) != 4:
    ANSWER = "".join(random.choices(string.digits, k=4))

print("Welcome to the Cows and Bulls Game!")
print("Bulls are digits in the right place")
print("Cows are digits in the wrong place")
print("Get 4 bulls to win!")
print("Enter a number:")
while True:
    num = input(">>> ")
    if (not num.isdigit()) or (len(num) != 4):
        print("Enter a 4 digit number!")
        continue
    bulls = count_bulls(num, ANSWER)
    print(f"{count_cows(num, ANSWER)} cows, {bulls} bulls")
    if bulls == 4:
        print("You win!")
        break
    
