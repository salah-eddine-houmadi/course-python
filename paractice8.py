#problem

month = "February"

months_31_days = ("January", "March", "May", "July", 
					"August", "October", "December")

months_30_days = ("April", "June", "September", "November")

if month in months_31_days:
	print(f"{month} has: 31 days")
elif month in months_30_days:
	print(f"{month} has: 30 days")
else:
	print(f"{month} has: 28 days")
	
#problem

a = 3
b = 2
c = 1

if a > b > c:
	print("Decreasing Order")
elif a < b < c:
	print("Increasing Order")
else:
	print("None")

#problem
	
import math

a = 2
b = 5 
c = -3

discriminant = b**2 - 4*a*c

if discriminant < 0:
	print("Complex Roots")
elif discriminant == 0:
	r = (-b + math.sqrt(discriminant))/(2*a)
	print(r)
else:
	r1 = (-b - math.sqrt(discriminant))/(2*a)
	r2 = (-b + math.sqrt(discriminant))/(2*a)
	print(r1, r2)
	
#problem

year = 1836

if year % 4 != 0:
	print(f"{year} is not a leap year")
elif year % 100 != 0:
	print(f"{year} is a leap year")
elif year % 400 != 0:
	print(f"{year} is not a leap year")
else:
	print(f"{year} is a leap year")

#problem

ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4
INTEGER_DIVISION = 5
MODULO = 6

print("=== Welcome to your Interactive Python Calculator ===")

a = int(input("Please enter the first value: "))
b = int(input("Please enter the second value: "))

print("Great! Now enter the operation.")
print("These are the available options:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Integer Division")
print("6 - Modulo")

operation = int(input("--> Enter the corresponding integer: "))

if operation == ADDITION:
	result = a + b
	print(f"The result of {a} + {b} is: {result}")
elif operation == SUBTRACTION:
	result = a - b
	print(f"The result of {a} - {b} is: {result}")
elif operation == MULTIPLICATION:
	result = a * b
	print(f"The result of {a} * {b} is: {result}")
elif operation == DIVISION:
	if b == 0:
		print("Division by Zero. Please enter another value for b.")
	else:
		result = a / b
		print(f"The result of {a} / {b} is: {result}")
elif operation == INTEGER_DIVISION:
	if b == 0:
		print("Division by Zero. Please enter another value for b.")
	else:
		result = a // b
		print(f"The result of {a} // {b} is: {result}")
elif operation == MODULO:
	result = a % b
	print(f"The result of {a} % {b} is: {result}")
else:
	print("Please choose a valid operation.")
	
#problem

import random

options = ("rock", "paper", "scissors")

computer = options[random.randint(0, 2)]

print("====== Welcome to the game ======")
player = input("Please enter Rock, Paper, or Scissors below:\n")

if player.lower() == computer:
    print("It's a tie! Try again.")
elif player.lower() == "rock":
    if computer == "paper":
        print("You lose! Your opponent chose 'Paper'")
    else:
        print("You win! Your opponent chose 'Scissors'") 
elif player.lower() == "paper":
    if computer == "scissors":
        print("You lose! Your opponent chose 'Scissors'")
    else:
        print("You win! Your opponent chose 'Rock'")
elif player.lower() == "scissors":
    if computer == "rock":
        print("You lose! Your opponent chose 'Rock'")
    else:
        print("You win! Your opponent chose 'Paper'")
else:
    print("Please enter a valid option.")
