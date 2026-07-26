import matplotlib.pyplot as plt

labels = ["Market-driven", "Both", "Neither"]
sizes = [5, 2, 3]
colors = ["pink", "yellow", "lightgreen"]

plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140)

plt.title("Lit analysis: Global North")
plt.show()

