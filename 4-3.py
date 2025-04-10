import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate random student scores
data = {
    'Student': ['A', 'B', 'C', 'D', 'E'],
    'Math': np.random.randint(60, 100, 5),
    'Science': np.random.randint(60, 100, 5),
}
df = pd.DataFrame(data)

# Display and visualize
print(df)
df.set_index('Student').plot(kind='bar', title="Student Scores")
plt.ylabel("Marks")
plt.show()
