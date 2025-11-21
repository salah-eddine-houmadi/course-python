#problem

for i in range(1,16):
    print(i)

#problem

n = int(input("Enter the value of 'n' :"))

for i in range(n, 0, -1):
    print(i)

#problem

total = 0

for i in range(1,101):
    total +=i

print(total)

#problem

n = int(input("Enter the value of 'n':"))

print(f"=============MULTiplication Table of {n} ======")
for i in range(1,11):
    print(f"{n} x {i} = {n * i}")

#problem

for i in range(65,91):
    print(chr(i))

#problem

for i in range(2,201,2):
    print(i)

#problem

n = int(input("Enter the valie of 'n' :"))

factorial = 1

for i in range(2, n+1):
    factorial *= i

print(factorial)