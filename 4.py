import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
df = sns.load_dataset('titanic')

# Basic data analysis
print("Average age by class:\n", df.groupby('class')['age'].mean())

# Visualization
sns.barplot(x='class', y='age', data=df)
plt.title("Average Age by Class on Titanic")
plt.show()
