import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

cases = ["A", "B", "C"]
newyork = [3.01, 11.32, 7.17]
singapore = [-10.4, -14.2, -18.24]

x = np.array([3, 4, 5])
width = 0.3
gap = 0.5

xn = x - 2
xs = x + 1

fig, ax = plt.subplots(figsize=(8,5))

one = ax.bar(xn, newyork,  width, label = "New York City", color="red")
two = ax.bar(xs, singapore, width, label = "Singapore", color="blue")

plt.ylabel("% Difference")
plt.xlabel("Case studies")
plt.title("RESIDENTIAL POPULATION")

legend = [mpatches.Patch(color="red", label="New York City"), mpatches.Patch(color="blue", label="Singapore")]

ax.legend(handles=legend, loc="upper right")

plt.axhline(y=0)

plt.show()

