#problem

def greet():
    print("Hello, Python Learner!")

greet()

#problem 

def square(x):
    return x*x
print(square(3))

#problem 

def full_name(first,last):
    return f"{first} {last}"

print(full_name("John", "Doe"))

#problem 

def calculate_area(length,width=10):
    return length * width

print(f"The area of this rectangle is {calculate_area(13,20)}")
print(calculate_area(13))

#problem 

square = lambda x: x*x
list1 = [1,2,3,4,5]

print(list(map(square,list1)))

#problem 

def factorial(n):
    if n == 0 or n== 1:
        return 1
    return factorial(n -1) * n

print(factorial(5))

#problem 

def sum_of_digits(n):
    if n == 0:
        return 0
    return n%10 + sum_of_digits(n//10)

print(sum_of_digits(7532))

#problem 

import math

a = math.sqrt(144)
b = math.sin(math.radians(90))
print(a,b)

#problem 

import requests

a = requests.get("https://api.github.com/")
print(a.json())

#problem 

def increment():
    counter = 0
    counter +=1
    print(counter)

increment()
increment()
increment()