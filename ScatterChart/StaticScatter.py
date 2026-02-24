import matplotlib.pyplot as plt

# Static (hardcoded) data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]

plt.figure(figsize=(7,5))
plt.scatter(x, y, color='blue')

plt.title("Static Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)

plt.show()
