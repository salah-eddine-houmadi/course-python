#problem1

def say_hello():
    print("hello")

#problem2

def sum_1m(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

a = sum_1m(10000)
print(a)

#problem3

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.5f} seconds")
        return result
    return wrapper

@timer
def sum_numbers():
    return sum(range(1, 1000001))

sum_numbers()


#problem4

class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Warning: Salary cannot be negative!")
        else:
            self._salary = value

emp = Employee(5000)
print(emp.salary)
emp.salary = -1000  
emp.salary = 7000
print(emp.salary)

#problem5

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        print("This is a utility class for math operations.")


print(MathUtils.add(5, 3))
MathUtils.description()

#problem5

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return len(self.title)

book1 = Book("1984", "George Orwell")
book2 = Book("Python 101", "Mike Driscoll")

print(book1)      
print(len(book2)) 

#problem6

class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise NegativeNumberError("You entered a negative number!")
    result = 10 / num
except ValueError:
    print("Invalid input! Not a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except NegativeNumberError as e:
    print(e)


#problem7

from functools import reduce


numbers = [1, 2, 3, 4, 5]
cubes = list(map(lambda x: x**3, numbers))
print(cubes)


nums = [10, 11, 12, 13, 14]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)


nums2 = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums2)
print(product)

#problem8

while (text := input("Enter text: ")) != "quit":
    print(f"You entered: {text}")


words = ["python", "rocks", "ai"]
lengths = [n for w in words if (n := len(w)) >= 4]
print(lengths)
