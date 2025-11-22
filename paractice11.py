#problem

my_list = [1,2,3,4]

def find_sum(s):
    if len(s) == 0:
        return 0
    else:
        return s[0] + find_sum(s[1:])

print(find_sum(my_list))

#problem
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else :
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0))

#problem
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(0))

#problem

def sum_of_digits(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sum_of_digits(num// 10)

print(sum_of_digits(55))

#problem

def calculate_power(a,b):
    if b == 1:
        return a 
    else:
        return a * calculate_power(a,b-1)
    
print(calculate_power(1,2))