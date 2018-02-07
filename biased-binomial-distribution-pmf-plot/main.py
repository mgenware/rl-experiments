import numpy as np
from scipy import special
import matplotlib.pyplot as plt
import sys

def pmf(p, n, k):
  return special.comb(n, k) * p**k * (1-p)**(n-k)

args = sys.argv[1:]
if len(args) != 2:
  print("Invalid arguments. Example: main.py 0.5 20")
  sys.exit(1)

p = float(args[0])
n = int(args[1])

print('p={:f}, n={:d}'.format(p, n))

x = np.linspace(0, n, 100)
vpmf = np.vectorize(pmf)
y = vpmf(p, n, x)

plt.plot(x, y, color='g')
plt.xlabel('N')
plt.ylabel('P')
plt.show()

