#Problem 1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect1 = Rectangle(5, 10)
print("Rectangle 1 Area:", rect1.area())
print("Rectangle 1 Perimeter:", rect1.perimeter())

#Problem 2
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Salary: {self.salary}")
        
emp1 = Employee("John Doe", "E123", 50000)
emp1.display_employee_info()

#Problem 3
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

class Bike(Vehicle):
    def move(self):
        print("Bike is cycling")

vehicle = Vehicle()
car = Car()
bike = Bike()

listOfObjs = [vehicle, car, bike]

for obj in listOfObjs:
    obj.move()

#Problem 4
class Vector:
    def __init__(self , x , y):
        self.x = x
        self.y = y

    def __sub__(self , other):
        return f"Vector({self.x - other.x} , {self.y - other.y})"
    
    def __mul__(self , other):
        return self.x * other.x + self.y * other.y

v1 = Vector(3 , 4)
v2 = Vector(2 , 1)
print(v1 - v2)
print(v1 * v2)

#Problem 5
import math
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self , radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self , width , height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

def print_shape_area(shape : Shape):
    print(f"The area of the shape is: {shape.area()}")

shapes = [Shape() , Circle(5) , Rectangle(2 , 10)]
for shape in shapes:
    print_shape_area(shape)