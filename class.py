# class Employee:
#     company = "HP"
#     def get_salary(self):
#         return 34000
    
# e = Employee()
# print(e.get_salary())

# e1 = Employee()
# print(e1.get_salary())

class Employee:
    company = "Assus"

    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name} . Salary is {self.salary}. The bond is for {self.bond} years")

    
e1 = Employee(34000, 'Johon Doe', 4)
e1.get_info()

print(e1.company)

#print(dir(e1))


class Animal:
    location = "Australia"
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

a = Animal("Dog")
a.speak()



class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def sum(self,p):
        return Point(self.x + p.x, self.y + p.y)
    def print_point(self):
        return (f"X is {self.x} and y is {self.y}")
    
    def __add__(self,p):
        return Point((self.x + p.x),(self.y + p.y))
    
p1 =Point(3,2)
p2 =Point(6,3)

#p = p1.sum(p2)
p = p1 + p2
p.print_point()

    