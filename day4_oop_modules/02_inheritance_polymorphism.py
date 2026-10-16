# Employee and Manager
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def total_pay(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

        def total_pay(self):
            return self.salary + self.bonus

e = Employee("Sachin", 30000)
m = Manager("Boss", 50000, 10000)
print(e.total_pay())
print(m.total_pay())


# Shapes(polymorphism)
import math

class Shape:
    def area(self):
        raise NotImplementedError("Child class must define area()")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

shapes = [Circle(7), Rectangle(4, 5)]
for shape in shapes:
    print(round(shape.area(), 2))