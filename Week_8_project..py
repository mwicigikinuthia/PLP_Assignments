# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set plot style
sns.set(style='whitegrid')

# Try loading the Iris dataset and converting it into a pandas DataFrame
try:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].apply(lambda x: iris.target_names[x])
except Exception as e:
    print("Error loading the dataset:", e)

# Display the first 5 rows of the dataset
print(df.head())

# Check the data types of each column
print(df.dtypes)

# Check for any missing values
print(df.isnull().sum())

# Display basic statistics for numeric columns
print(df.describe())

# Group the dataset by species and calculate the mean of each measurement
grouped = df.groupby('species').mean()
print(grouped)

# Line chart showing average sepal length per species
plt.figure(figsize=(8,5))
grouped['sepal length (cm)'].plot(kind='line', marker='o')
plt.title("Average Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.grid(True)
plt.show()

# Bar chart showing average petal length per species
plt.figure(figsize=(8,5))
sns.barplot(x='species', y='petal length (cm)', data=df, ci=None, palette='pastel')
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# Histogram showing distribution of sepal width
plt.figure(figsize=(8,5))
plt.hist(df['sepal width (cm)'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# Scatter plot comparing sepal length and petal length, colored by species
plt.figure(figsize=(8,5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.show()
