import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 175, 10
heights = sigma * np.random.randn(100) + mu
print(heights)

hist = plt.hist(heights, bins=20, edgecolor='black', linewidth=1)
plt.show()
