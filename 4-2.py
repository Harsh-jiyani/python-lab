import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Generate random scores
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
scores = {
    'Math': np.random.randint(60, 100, size=5),
    'Science': np.random.randint(60, 100, size=5),
    'English': np.random.randint(60, 100, size=5)
}

# Step 2: Create DataFrame
df = pd.DataFrame(scores, index=students)
print(" Student Score Table:\n")
print(df)

# Step 3: Plot the scores
df.plot(kind='bar', figsize=(8, 5), title='Student Scores by Subject')
plt.ylabel("Marks")
plt.xlabel("Students")
plt.grid(True)
plt.tight_layout()
plt.show()
