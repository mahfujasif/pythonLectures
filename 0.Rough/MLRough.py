import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])

plt.scatter(x_train, y_train, marker='x', c='r')
# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sqft)')
plt.show()
