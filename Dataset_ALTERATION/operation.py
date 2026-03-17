import csv
import matplotlib.pyplot as plt
import numpy as np

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
        ages.append(float(row['Age']) if row['Age'] != '' else None)
        salaries.append(float(row['Salary']) if row['Salary'] != '' else None)
        scores.append(float(row['Score']) if row['Score'] != '' else None)

# 2. Function to calculate mean
def mean(values):
    valid = [v for v in values if v is not None]
    return sum(valid) / len(valid) if len(valid) > 0 else 0

# 3. Calculate means
age_mean = mean(ages)
salary_mean = mean(salaries)
score_mean = mean(scores)

# 4. Fill missing values
ages = [v if v is not None else age_mean for v in ages]
salaries = [v if v is not None else salary_mean for v in salaries]
scores = [v if v is not None else score_mean for v in scores]

# 6. BETTER COMBO BAR CHART
fig, ax1 = plt.subplots(figsize=(10, 6))

# Create bars for Age and Score (Left Axis)
labels = ['Age', 'Score']
means = [age_mean, score_mean]
x = np.arange(len(labels))
width = 0.35

rects1 = ax1.bar(x, means, width, label='Metrics', color=['skyblue', 'orange'])
ax1.set_ylabel('Age / Score Value')
ax1.set_title('Comparison of Average Age, Score, and Salary')
ax1.set_xticks(x)
ax1.set_xticklabels(labels)

# Create a second y-axis for Salary
ax2 = ax1.twinx()
ax2.bar([2], [salary_mean], width, label='Salary', color='lightgreen')
ax2.set_ylabel('Salary Value')
ax2.set_xticks([0, 1, 2])
ax2.set_xticklabels(['Avg Age', 'Avg Score', 'Avg Salary'])

plt.show()

# 7. PIE CHART (Score categories)
low, medium, high, very_high = 0, 0, 0, 0
for s in scores:
    if s <= 60: low += 1
    elif s <= 75: medium += 1
    elif s <= 90: high += 1
    else: very_high += 1

plt.figure()
plt.pie([low, medium, high, very_high], labels=['Low', 'Medium', 'High', 'Very High'], autopct='%1.1f%%')
plt.title("Score Distribution")
plt.show()

# 8. STEP CHART (Salary trend)
plt.figure()
plt.step(ids, salaries, where='mid', color='purple')
plt.title("Salary Trend")
plt.show()
