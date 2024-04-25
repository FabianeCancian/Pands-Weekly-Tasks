# https://www.w3schools.com/python/numpy/numpy_random_normal.asp

#Creating the values for the plot. This function will return the values accdording to Mean (loc) 5 and SD (scale) 2
from numpy import random
values = random.normal(loc=5, scale=2, size=(10, 100))
print(values)

import numpy as np 
import matplotlib.pyplot as plt

# Plotting the histogram, defining the plot colour, width, title and X and Y axis label.
plt.hist(values, bins=8, linewidth=5, edgecolor="blue")
plt.title("Random Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()

#Resolving h(x)=x3  to generate values reported on the plot.
x=np.array([0,1,2,3,4,5,6,7,8,9,10])
h =(x**3)
print (h)

# Creating the visual representaiton (plot)

plt.bar(x, h, linewidth=5, color="green")
plt.title("h(x)=x3")
plt.xlabel("Nomal vlaue, from 0 to 10")
plt.ylabel("Exponencial value")
plt.show()
