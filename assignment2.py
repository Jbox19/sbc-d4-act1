
from random import randint
"""
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

result1 = randint(0,9)
result2 = randint(0,9)
result3 = randint(0,9)


print("Your Bet: ", number1, number2, number3)
print("Result: ", result1, result2, result3)

if number1 == result1 and number2 == result2 and number3 == result3:
    print("You Win!")
elif (number1 == result1 and number2 == result3 and number3 == result2) or (number1 == result3 and number2 == result1 and number3 == result2) or (number1 == result2 and number2 == result1 and number3 == result3) or (number1 == result3 and number2 == result1 and number3 == result2) or (number1 == result3 and number2 == result2 and number3 == result1):
    print("You Partially Win!")
else:
    print("You lose!")
"""

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
bet = f"{number1} {number2} {number3}"

result1 = randint(0,9)
result2 = randint(0,9)
result3 = randint(0,9)
result = f"{result1} {result2} {result3}"

print("Your Bet: ", bet)
print("Result: ", result)

if bet == result:
    print("You Win!")
else:
    bett = {number1, number2, number3}
    resultt = {result1, result2, result3}
    if bett == resultt:
        print("You Partially Win!")
    else:
        print("You lose!")