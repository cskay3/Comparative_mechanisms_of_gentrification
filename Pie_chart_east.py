import matplotlib.pyplot as plt

labels = ["Market-driven", "Tenure-conversion", "Both", "Neither"]
sizes = [2, 4, 1, 3]
colors = ["pink", "lightblue", "yellow", "lightgreen"]

plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors)

plt.title("Lit analysis: Global East")
plt.show()
