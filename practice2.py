#problem

s = "Hello, World!"
new_s = ""

COMMA = ","
DOT = "."

for char in s:
    if char == COMMA:
        new_s += DOT
    else:
        new_s += char

print(new_s)

#problem

s = "Hello, World!"
COMMA = ","
DOT = "."

print(s.replace(COMMA, DOT))

#problem

import string
s = "The quick brown fox jumps over the lazy dog"

set_s = set(s.lower())
set_s.remove(" ")
print(set_s == set(string.ascii_lowercase))

#problem

import string

s = "The quick brown fox jumps over the lazy dog"
is_pangram = True

for char in string.ascii_lowercase:
    if char not in s.lower():
        is_pangram = False
        break

print(is_pangram)

#problem

s = "Hello,World!"
new_s = ""

for char in s:
    if char != " ":
        new_s += char
print(new_s)


#problem

s = "Hello"
prefix = "He"

print(s[len(prefix)] == prefix)


#problem

s = "Coding"
suffix = "eng"

print(s[-len(suffix):] == suffix)

#problem

s = "Hello"
suffix = "ello"

print(s.endswith(suffix))

#problem

s = "Hello World"

words_list = s.split()
new_s = ""

for word in words_list:
    reversed_word = "".join(reversed(word))
    swapped_case = reversed_word.swapcase()
    new_s += swapped_case + " "

new_s = new_s.rstrip()
print(new_s)


#problem

s = "Hello"

repeated_count = 0
repeated_chars = []

for char in s:
    if(s.count(char) > 1) and (char not in repeated_chars):
        repeated_count += 1
        repeated_chars.append(char)

print(repeated_count)

#problem

s = "Hello World"
new_s = ""

words_list = s.split(" ")
for word in words_list:
    new_s += "".join(sorted(word.lower())) + " "
    
new_s.rstrip()
print(new_s)