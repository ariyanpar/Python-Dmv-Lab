import csv
import matplotlib.pyplot as plt

# File name
filename = "dataset_sample.csv"

# Lists to store data
ids = []
ages = []
salaries = []
scores = []

# 1. Read CSV and handle missing values
with open(filename, 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        ids.append(int(row['ID']))

        # Convert or mark missing as None
        ages.append(float(row['Age']) if row['Age'] != '' else None)
        salaries.append(float(row['Salary']) if row['Salary'] != '' else None)
        scores.append(float(row['Score']) if row['Score'] != '' else None)

# 2. Function to calculate mean ignoring None
def mean(values):
    valid = [v for v in values if v is not None]
    return sum(valid) / len(valid) if len(valid) > 0 else 0

# 3. Calculate means
age_mean = mean(ages)
salary_mean = mean(salaries)
score_mean = mean(scores)

# 4. Count missing values
print("Missing Values:")
print("Age:", ages.count(None))
print("Salary:", salaries.count(None))
print("Score:", scores.count(None))

# 5. Fill missing values with mean
ages = [v if v is not None else age_mean for v in ages]
salaries = [v if v is not None else salary_mean for v in salaries]
scores = [v if v is not None else score_mean for v in scores]

print("\nMissing values filled!")

# 6. BAR CHART (Average values)
labels = ['Age', 'Salary', 'Score']
avg_values = [age_mean, salary_mean, score_mean]

plt.figure()
plt.bar(labels, avg_values, color=['blue', 'green', 'orange'])
plt.title("Average Values")
plt.ylabel("Value")
plt.show()

# 7. PIE CHART (Score categories)
low = 0
medium = 0
high = 0
very_high = 0

for s in scores:
    if s <= 60:
        low += 1
    elif s <= 75:
        medium += 1
    elif s <= 90:
        high += 1
    else:
        very_high += 1

sizes = [low, medium, high, very_high]
labels = ['Low', 'Medium', 'High', 'Very High']

plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Score Distribution")
plt.show()

# 8. STEP CHART (Salary trend)
plt.figure()
plt.step(ids, salaries, where='mid', color='purple')
plt.title("Salary Trend (Step Chart)")
plt.xlabel("ID")
plt.ylabel("Salary")
plt.show()