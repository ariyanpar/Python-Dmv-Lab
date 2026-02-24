import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = []

for c in categories:
    val = int(input(f"Enter value for {c}: "))
    values.append(val)

plt.bar(categories, values)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart from User Input')
plt.show()
1