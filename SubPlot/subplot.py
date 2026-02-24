import matplotlib.pyplot as plt

# Static data
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 40]
y2 = [40, 30, 25, 20, 10]

# Create 2 subplots (2 rows, 1 column)
fig, axs = plt.subplots(2, 1, figsize=(6, 8))

# First subplot
axs[0].plot(x, y1, marker='o', color='blue')
axs[0].set_title("First Plot")
axs[0].set_xlabel("X Values")
axs[0].set_ylabel("Y1 Values")
axs[0].grid(True)

# Second subplot
axs[1].plot(x, y2, marker='s', color='red')
axs[1].set_title("Second Plot")
axs[1].set_xlabel("X Values")
axs[1].set_ylabel("Y2 Values")
axs[1].grid(True)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()
