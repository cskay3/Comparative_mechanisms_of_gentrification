import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

cases = ["A", "B", "C"]
newyork = [5, 6, 7]
singapore = [4, 3, 2]

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
plt.title("INCOME")

legend = [mpatches.Patch(color="red", label="New York City"), mpatches.Patch(color="blue", label="Singapore")]

ax.legend(handles=legend, loc="upper left")

plt.show()

