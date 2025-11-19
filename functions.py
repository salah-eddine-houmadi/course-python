# a = 4
# b = 2
# c = 1

# average = (a + b + c)/3
# print(average)

# a1 = 6
# b1 = 7
# c1 = 12

# average = (a1 + b1 + c1)/3
# print(average)

def average(a,b,c):
    d =(a+b+c)/3.0
    #print(d)
    return d

o1 =average(3,5,8)
o2 =average(4,2,1)

print(o1)
print(o2)

def add(a,b):
    x = a + b
    return x

x = add(3,5)
print(x)


square = lambda x: x*x
# def square(x):
#     return x*x
sum = lambda x,y: x+y
# def sum(x,y):
#     return x+y
print(square(3))
print(sum(3,62))



def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-2) + fib(n-1)

print(fib(6))


import math
import os
print(math.sqrt(16))

def sum(a,b):
    # local
    c= a+b
    z = 1
    return c
#global
z = 8
print(sum(4,6))
print(z)



def sum(a,b):
    print("hey I am summing")
    c = a + b
    global z
    z = 0
    return c

z = 3
print(sum(3,12))
print(z)