#Problem 1
import this

#Problem 2
import dis

def square(x):
    return x * x

dis.dis(square)

#Problem 3
data = 10
print(type(data))     # int
data = [1, 2, 3]
print(type(data))     # list
def my_func():
    pass
data = my_func
print(type(data))     # function

#Problem 5
import ast

code = "y = (4 * 5) - 3"
tree = ast.parse(code)
print(ast.dump(tree, indent=4))

#Problem 6
my_list = [10,20,30]
print(id(my_list))
my_list.append(40)
print(id(my_list))