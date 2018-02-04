import sys
import math

# https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
def nCr(n,r):
  f = math.factorial
  return f(n) / f(r) / f(n-r)

args = sys.argv[1:]
if not len(args):
  sys.exit(1)
n = int(args[0])
if n <= 0:
  sys.exit(2)

print('n: ', n)

for x in range(0, n):
  res = int(nCr(n - 1, x))
  print(res , end=' ', flush=True)
print()
