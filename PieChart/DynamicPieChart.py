import matplotlib.pyplot as plt

labels = []
sizes = []

n = int(input("Enter number of categories: "))

for i in range(n):
    label = input(f"Enter name of category {i+1}: ")
    value = float(input(f"Enter value for {label}: "))
    
    labels.append(label)
    sizes.append(value)

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels,
        autopct='%1.1f%%', startangle=90)

plt.title("Dynamic Pie Chart")
plt.axis('equal')
plt.show()
