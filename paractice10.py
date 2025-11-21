#problem

num = int(input("Enter an integer: "))

if num == 0 or num == 1:
	print("Not Prime")
else:
	for i in range(2, num):
		if num % i == 0:
			print("Not Prime")
			break
	else:
		print("Prime")
		
#problem

n = int(input("Enter the value of 'n':"))

for i in range(1, n+1):
	print("*" * i)

#problem

num = 352

reverse = int(str(num)[::-1])
print(reverse)

#problem
s = "hello"

for char in s[::-1]:
	print(char,end="")

#problem

n = int(input("Enter the number of rows: "))

k = (2 * n) - 2

for i in range(n):

    for j in range(k):
        print("", end=" ")

    for j in range(i + 1):
        print("*", end=" ")

    print("")

    k = k - 2

#problem

n = int(input("Enter the number of rows: "))

count = 1

for i in range(1, n+1):
    for j in range(0, i):
        print(count, end=" ")
        count += 1
    print()


#problem

num_rows = int(input("enter the number of rows:"))

for i in range(0, num_rows):
	print(chr(65 + i) * (i +1))

#problem

height = int(input("Enter the diamond's height (an odd number): "))

if height % 2 == 0:
    print("Please enter an odd value for the height (number of rows).")
else:
    middle_rows = (height + 2) // 2

    for i in range(middle_rows):
        print(" " * (middle_rows - i), "*" * (i*2 + 1))

    for i in range(middle_rows-2, -1, -1):
        print(" " * (middle_rows - i), "*" * (i*2 + 1))