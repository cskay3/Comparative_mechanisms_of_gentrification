#imports python packages
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#cases and data points (residential population differences) 
cases = ["A", "B", "C"]
newyork = [24.54, 48.06, 26.97]
singapore = [40.96, 43.05, 39.11]

#creates an array
x = np.array([3, 4, 5])
width = 0.3
gap = 0.5

#horizontally seperates the 2 bar graphs (new york vs singapore)
xn = x - 2
xs = x + 1

#sets the size of the bar graphs
fig, ax = plt.subplots(figsize=(8,5))

#creates 2 sets of bar graphs with the data from the sets of new york & singapore
one = ax.bar(xn, newyork,  width, label = "New York City", color="red")
two = ax.bar(xs, singapore, width, label = "Singapore", color="blue")

#adds labels for x and y axis
plt.ylabel("% Difference")
plt.xlabel("Case studies")
plt.title("INCOME: change from 2010~2020")

#adds a legend to distinguish the different cities
legend = [mpatches.Patch(color="red", label="New York City"), mpatches.Patch(color="blue", label="Singapore")]

#adds a horizontal line at y=0 through the graph
ax.legend(handles=legend, loc="upper right")

#produces bar graph
plt.show()
