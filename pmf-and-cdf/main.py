import numpy as np
import matplotlib.pyplot as plt

colors = ['gold', 'yellowgreen', 'c', 'royalblue', 'pink']

# randomly generate the number of occurrences of each color
occurrences = np.random.randint(10, size=len(colors)) + 1
# pmf of the distribution
sum = np.sum(occurrences)
pmf = occurrences / sum

print(pmf)

# plot pmf
bars = np.arange(len(colors))
fig, ax = plt.subplots(2)

ax[0].bar(bars, pmf, color=colors)
ax[0].set_xticks(bars)
ax[0].set_xticklabels(colors)

# plot cdf
cdf = np.cumsum(pmf)
ax[1].step(bars, cdf, where='mid')
ax[1].set_xticks(bars)
ax[1].set_xticklabels(colors)

print(cdf)

plt.show()
