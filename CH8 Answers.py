#Problem 1
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(f"Mean: {arr.mean()}")
print(f"Median: {np.median(arr)}")
print(f"Standard Deviation: {arr.std()}")

# Problem 2
import pandas as pd

students = pd.DataFrame({
    "Name": ["Ali", "Mona", "Omar", "Sara"],
    "Age": [20, 22, 19, 21],
    "Score": [85, 92, 78, 88]
})
high_scores = students[students["Score"] > 80]
print(f"Students with score above 80: \n{high_scores}")

#Problem 3
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Graph of y = x^2")

plt.show()

# Problem 4
from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, Advanced Python!"

if __name__ == "__main__":
    app.run()

#Problem 5
import torch

a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

dot_product = torch.dot(a, b)
elementwise_mult = a * b
print(f"Dot Product: {dot_product}")
print(f"Element-wise Multiplication: {elementwise_mult}")