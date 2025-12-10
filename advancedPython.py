def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def say_hello(a):
    print(f"Hello! {a}")

say_hello("Harry")

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def first_name(self,first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name
    def __str__(self):
        return f"the name is {self.name} and the salary is {self.salary}"
    def __repr__(self):
        return f"name: {self.name}\nsalary:{self.salary}"
    def __len__(self):
        return len(self.name)
        

e = Employee("Jack doe" , 34555)
print(len(e))
print(e.first_name)
e.first_name = "John"
print(e.name)


