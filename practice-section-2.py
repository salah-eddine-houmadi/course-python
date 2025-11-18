#problem

str1 = "Hello"
str2 = "World"

print(str1 + "" + str2)
print(str1,str2)

#problem

text = "Python Programming"

print(text[0:6])
print(text[-6:])

#problem

name = "Harry"

print(name[0])
print(name[-1])
print(len(name))


#problem

str1 = "123abc"

if str1.isalnum():
    print("Yes this string is alphanumeric")
else:
    print("This string is not alphanumeric")


#problem

name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")


#problem
sentence = "Coding in python is fun fun"
new = sentence.replace("fun", "awesome")

print(new)