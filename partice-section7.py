#problem1

class Car:
    def drive(self):
        print("Car is poving")

car1 = Car()
car1.drive()

#problem2

class Person:
    def __init__(self, name,age):
        self.name = name 
        self.age = age

p1 = Person("John Doe" , 45)
print(p1.name, p1.age)

#problem3

class Animal:
    def sound(self):
        print("Some sound")

class Dog:
    def sound(self):
        print("Bark!")

a = Animal()
a.sound()

b = Dog()
b.sound()
    
