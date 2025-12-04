#Problem 1
from dataclasses import dataclass

@dataclass
class Vector3D:
    x: float
    y: float
    z: float
    
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)  

#Problem 2

class Positive:
    def set(self,value):
        if value < 0:
            raise ValueError("Value must be non-negative!")


class BankAccount:
    balance = Positive()

    def __init__(self, balance):
        self.balance = balance  # الحارس بيتأكد من القيمة


acc = BankAccount(-10)
print(acc.balance)     # 100

acc.balance = 50       # OK
acc.balance = -10    # ERROR → ValueError

#Problem 3

class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(5, 10)
print(p.x, p.y)

p.z = 5

#Problem 4

def calculate_sum(a , b):
    return a + b

import dis

dis.dis(calculate_sum)
#Problem 1
from dataclasses import dataclass

@dataclass
class Vector3D:
    x: float
    y: float
    z: float
    
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)  

#Problem 2

class Positive:
    def set(self,value):
        if value < 0:
            raise ValueError("Value must be non-negative!")


class BankAccount:
    balance = Positive()

    def __init__(self, balance):
        self.balance = balance  # الحارس بيتأكد من القيمة


acc = BankAccount(-10)
print(acc.balance)     # 100

acc.balance = 50       # OK
acc.balance = -10    # ERROR → ValueError

#Problem 3

class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(5, 10)
print(p.x, p.y)

p.z = 5

#Problem 4

def calculate_sum(a , b):
    return a + b

import dis

dis.dis(calculate_sum)