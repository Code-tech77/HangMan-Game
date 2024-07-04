import numpy as np
import matplotlib.pyplot as plt

my_x = np.linspace(-1,1)
my_y = np.sin(my_x)
plt.plot(my_x,my_y)

title = "Plot"
filename = "plot.jpg"

plt.title(title)
