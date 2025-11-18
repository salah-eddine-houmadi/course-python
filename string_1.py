name = "harry012345678"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])

# print(name[-1])
# print(name[-2])
# print(name[-3])
# print(name[-4])
# print(name[-5])

print(name[0:2])
print(name[2:-1])
print(name[0:10:1])
print(name[0:10:2])

print(name[:4])
print(name[1:])

a = len(name)
print(a)

s= "hello world"

a = len(s)
print(a)
print(s.upper())
print(s.lower())
print(s.capitalize())

# text = "Python is fun and fun and fun"
# print(text.find("is"))
# print(text.replace("fun", "awesome"))

# text = "Apples,bananas,Pineapple"
# print(text.split(","))
# print(",".join(['Apples', 'Bananas', 'Pineapples']))

# text = "Python123"
# print(text.isalpha())
# print(text.isdigit())
# print(text.isalnum())
# print(text.isspace())

template = "Dear {}, You are awesome. Taake this {} $ bag"
a = "salah"
a1 = 10000
b = "jack"
b1 = 5000
c = "Marie"
c2 = 200
s1 =template.format(a, a1)
print(s1)
print(f"{a} you are awesome and take this{a1} $ bag")