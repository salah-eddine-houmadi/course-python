#problem
s = "Python"

print(len(s))

#problem

s = "Hello"
i = 10

if len(s) == 0:
    print("Empty String")
elif i < len(s):
    print(s[i])
else:
    print("i out of range")

#problem

s = "Hello"
print(s[::-1])

# string[start:stop:step]

s = "hello"
reversed_word = "".join(reversed(s))
print(reversed_word)

#problem

s = "Wonderful"

if len(s)< 6:
    print("")
else:
    new_string = s[:3] + s[len(s)-3]
    print(new_string)

#problem

s = "Coding"
new_s = ""

for i in range(len(s)):
    if i % 2 != 0:
        new_s += s[i]

print(new_s)

for i in range(1,len(s),2):
    new_s += s[i]
print(new_s)

#problem

s = "Hello"

print(s.isdecimal())

#problem

s = "hello"
n = 1

if(len(s) == 0) or (n >= len(s)):
    print(s)
else:
    new_s = ""
    for i in range(len(s)):
        if i != n:
            new_s += s[i]
    print(new_s)

#problem

s = "Hello"
new_s = ""

curr_char = "L"
new_char = "s"

for char in s:
    if char == curr_char:
        new_s += new_char
    else:
        new_s += char

print(new_s)

#problem

s = "Python"

curr_char = "P"
new_char = "a"

print(s.replace(curr_char, new_char))
