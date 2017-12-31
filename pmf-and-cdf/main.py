import numpy as np
import matplotlib.pyplot as plt

colors = ['gold', 'yellowgreen', 'c', 'royalblue', 'pink']

# randomly generate the number of occurrences of each color
occurrences = np.random.randint(10, size=len(colors))
# pmf of the distribution
sum = np.sum(occurrences)
pmf = occurrences / sum

print(pmf)

# plotting
bars = np.arange(len(colors))
fig, ax = plt.subplots(2)

ax[0].bar(bars, pmf, color=colors)
ax[0].set_xticks(bars)
ax[0].set_xticklabels(colors)

plt.show()
