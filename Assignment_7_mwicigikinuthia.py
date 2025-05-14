# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset

try:
    # Load Iris dataset from sklearn
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].apply(lambda x: iris.target_names[x])

    print("First 5 rows of the dataset:")
    print(df.head())

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())


except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)



print("\nBasic statistics of numerical columns:")
print(df.describe())

# Group by species and calculate the mean of each feature
print("\nAverage measurements per species:")
grouped = df.groupby('species').mean()
print(grouped)

# Observations
print("\nInsights:")
print("- Versicolor and Virginica species tend to have longer petal lengths.")
print("- Setosa has the smallest petal and sepal measurements.")



sns.set(style="whitegrid")

# 1. Line Chart: Average sepal length over species (simulating trend)
plt.figure(figsize=(8,5))
grouped['sepal length (cm)'].plot(kind='line', marker='o')
plt.title("Average Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.grid(True)
plt.show()

# 2. Bar Chart: Average petal length per species
plt.figure(figsize=(8,5))
sns.barplot(x='species', y='petal length (cm)', data=df, ci=None, palette='viridis')
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram: Distribution of sepal width
plt.figure(figsize=(8,5))
plt.hist(df['sepal width (cm)'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot: Sepal length vs Petal length
plt.figure(figsize=(8,5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.show()

