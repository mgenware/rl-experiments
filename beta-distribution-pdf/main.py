import numpy as np
import math
from scipy import special
import matplotlib.pyplot as plt
import sys

def pdf(x, a, b):
  return math.gamma(a + b) / (math.gamma(a) * math.gamma(b)) * x**(a - 1) * (1 - x)**(b-1)

args = sys.argv[1:]
if len(args) != 2:
  print("Invalid arguments. Example: main.py 2 5")
  sys.exit(1)

a = int(args[0])
b = int(args[1])

print('a={:d}, b={:d}'.format(a, b))

x = np.linspace(0, 1.0, 100)
vpmf = np.vectorize(pdf)
y = vpmf(x, a, b)

plt.plot(x, y, color='g')
plt.xlabel('N')
plt.ylabel('P')
plt.show()

