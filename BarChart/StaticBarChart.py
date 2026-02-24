import matplotlib
import matplotlib.pyplot as plt

categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [10, 15, 7, 12]

plt.bar(categories, values)
plt.xlabel('Fruits')
plt.ylabel('Quantity')
plt.title('Fruit Inventory')

plt.show()
