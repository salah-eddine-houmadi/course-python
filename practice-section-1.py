# problem1
num = int(input("Enter a number :"))
print(num)

if(num<0):
    print("Number is negative !")
elif(num >0):
    print("Number is positive !")
else:
    print("Number is 0")

#problem2

age = int(input("Enter your age :"))

if(age>=18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote !")

#problem3

num = int(input("Enter your number"))

if(num%2 == 0):
    print("This number is even")
else:
    print("This number is odd")


#problem4

num = int(input("Enter a number\n"))

match num:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    
#problem5

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

operation = input("Choose operation :")

match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)

#problem

for i in range(1,11):
    print(i)

#problem

n = int(input("Enter your number :"))

for i in range(1,11):
    print(n, "X", i, "=", n*i)

#problem
for i in range(1,101):
    print(i)

#problem
sum = 0
for i in range(1,101):
    print(i)
    sum += i
print(sum)

#problem
for i in range(1,5):
    print("*"*i)

#problem

sum = 0
i = 1
while i<=100:
    sum +=i
    i += 1

print(sum)

#problem
password = "123AZE"
entered_pass =input("Enter Password :")

while (entered_pass != password):
    entered_pass = input("Wrong Password! try again and ent enter Password :")

print("Success! You are logged in")

#problem 

num = 45222
print(int(str(num)[::-1]))

#problem 
for i in range(1,11):
    if( i==7):
        break
    print(i)

#problem 
for i in range(1,11):
    if( i==5):
        continue
    print(i)

#problem 
for i in range(1,6):
    match i:
        case 1:
            print(1)
        case 2:
            print(2)
        case 3:
            print(3)
        case 4:
            print(4)
        case 5:
            print(5)