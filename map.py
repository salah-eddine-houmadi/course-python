number = [1,2,3,45,4,21]

# def square(x):
#     return x * x

new = list(map(lambda x:x*x, number))
print(new)

# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False
    
a = [1,3,55,2578,35,155,2156,8,254,7,3,43]
new = list(filter(lambda x:x>9, a))
print(new)


from functools import reduce

numbers = [1,2,3,4,5,6]

def sum(a,b):
    return a+ b

c = reduce(sum,number)
print(c)


def sum(*args):
    total = 0
    for item in args:
        total += item
    return total

print(sum(342,2,7,9))