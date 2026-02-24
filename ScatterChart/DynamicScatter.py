import matplotlib.pyplot as plt

# Take number of points from user
n = int(input("Enter number of points: "))

x = []
y = []

# Take x and y values from user
for i in range(n):
    x_val = float(input(f"Enter x value for point {i+1}: "))
    y_val = float(input(f"Enter y value for point {i+1}: "))
    x.append(x_val)
    y.append(y_val)

plt.figure(figsize=(7,5))
plt.scatter(x, y, color='red')

plt.title("Dynamic Scatter Plot (User Input)")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)

plt.show()
