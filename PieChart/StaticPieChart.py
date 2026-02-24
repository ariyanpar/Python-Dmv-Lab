import matplotlib.pyplot as plt

# Static data
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]
colors = ['gold', 'lightblue', 'lightcoral', 'lightskyblue']

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=90)

plt.title("Programming Language Popularity (Static)")
plt.axis('equal')  # Keeps pie circular
plt.show()
