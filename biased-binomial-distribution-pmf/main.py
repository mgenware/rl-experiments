import numpy as np
from scipy import special
import sys

def pmf(p, n, k):
  return special.comb(n, k) * p**k * (1-p)**(n-k)

args = sys.argv[1:]
if len(args) != 3:
  print("Invalid arguments. Example: main.py 0.5 20 10")
  sys.exit(1)

p = float(args[0])
n = int(args[1])
k = int(args[2])

print('p={:f}, n={:d}, k={:d}'.format(p, n, k))
print('result:', pmf(p, n, k))
