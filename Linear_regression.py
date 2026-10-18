#import libraries
from sklearn.datasets import load_diabetes
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = load_diabetes(as_frame=True).data[['s1', 's2']]

# Plot the data
plt.figure()
sns.scatterplot(data=df, x='s1', y='s2')
plt.show()
plt.close()