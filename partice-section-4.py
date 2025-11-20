#problem

fruits = ["apple", "banana" , "cherry"]

print(fruits[0])
fruits[1] = "orange"
print(fruits)
print(len(fruits))

#problem

list1 = [i for i in range(1,11)]
print(list1)
print(list1[0:3])
print(list1[-3:])

#problem

numbers = [5,2,9,1,7]
numbers.sort()
numbers.append(10)
numbers.remove(2)
print(numbers)

#problem

names = ["ali", "Bob","salah"]

names.insert(1,"David")
print(names)

#problem

coordinates = (10,20)
print(coordinates[0])
print(coordinates[1])

corList = list(coordinates)
corList[0] = 50
coordinates = tuple(corList)
print(coordinates)

#problem

my_set = {1,2,3,3,4}
print(my_set)

my_set.add(5)
my_set.remove(2)
print(my_set)

#problem

student = {"name":"Slah","age": 20,"grade":"A"}
print(student['name'])
student['grade'] = 'A+'
print(student)


#problem

myDict = {
    "Harry":2555552,
    "John Doe":6666336,
    "Donald trump":56566
}

print(myDict.keys())
print(myDict.values())

for key, value in myDict.items():
    print(key, value)


