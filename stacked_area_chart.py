import numpy as np
import matplotlib.pyplot as plt

# Generate random data
group_one = np.random.randint(1, 10, 10)
group_two = np.random.randint(1, 10, 10)
group_three = np.random.randint(1, 10, 10)

# Create the stacked area chart
y = np.row_stack((group_one, group_two, group_three))
x = np.arange(10)
y1, y2, y3 = (group_one, group_two, group_three)

ax = plt.subplot()
ax.stackplot(x, y)

# Labels
plt.title("Stacked area chart example")
plt.xlabel("X label")
plt.ylabel('Y label')
plt.show()