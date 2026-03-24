import numpy as np
import matplotlib.pyplot as plt

# Generate random data
x = np.random.rand(50)
y = -x + np.random.normal(0, 0.1, 50)

# Add an outlier
x = np.append(x, 0.2)
y = np.append(y, 2)

# Create scatter plot
plt.scatter(x, y)

# Labels and title
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Negative correlation with outlier")

# Show plot
plt.show()