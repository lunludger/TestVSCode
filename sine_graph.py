# importing packages or libraries to pythin file
import matplotlib.pyplot as plt
import numpy as np

# We can create a quick dataset using Numpy and visualise the data using matplotlib
x = np.linspace(0, 100, 100)  # x axis
y = np.sin(x) # y values
 
# Plot the data
plt.plot(x, y)

# Create a title
plt.title("My first matplotlib sine graph")

# Show the plot
plt.show()
