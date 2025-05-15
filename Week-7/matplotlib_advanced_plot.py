import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)
y2 = np.cos(x)

# Line Plot
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)', color='blue')
plt.plot(x, y2, label='cos(x)', color='orange')
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='red', label='sin(x)')
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# Bar Plot
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 5, 2]

plt.figure(figsize=(6, 4))
plt.bar(categories, values, color='green')
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Histogram
data = np.random.randn(1000)

plt.figure(figsize=(6, 4))
plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
