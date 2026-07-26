import matplotlib.pyplot as plt

labels = ["Market-driven", "Both", "Neither"]
sizes = [3, 3, 4]
colors = ["pink", "yellow", "lightgreen"]

plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors)

plt.title("Lit analysis: Global South")
plt.show()
