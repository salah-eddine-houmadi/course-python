marks = [54,23,54,93]
mixed = [43,"hello",False]

print(marks)
print(mixed)
print(marks[2:4])

marks.append(63)
marks.pop(1)
print(marks)

# a = 5
# table = []

# for i in range(1,11):
#     table.append(5*i)

table = [5*i for i in range(1,11)]

print(table)


a = (3,2,22,13)

print(a)
print(a[2])

t = (3,12,1,54,23,12)

print(t.count(12))
print(t.index(12))

s = {3,23,2,11}
print(s,type(s))

s = {34,23,1,3,22}
print(s)

s.add(32)
s.remove(1)
print(s)

a = {3,23,1}
b = {23,4,2,55,1}

c = a.union(b)
print(c)

d = a.intersection(b)
print(d)


marks = {"harry":34, "jack":24, "lily":94}

print(marks,type(marks))
print(marks["lily"])
marks["harry"] = 3
print(marks)

print(marks.keys())
print(marks.values())
#marks.clear()
marks.pop("lily")
print(marks)

table_of_5 = {i: 5*i for i in range(1,11)}
print(table_of_5)