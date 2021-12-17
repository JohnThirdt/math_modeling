import numpy as np
def vch(z, l, N):
  a = np.linspace(z, l, N)
  b = np.zeros(N)
  for i in range (N):
    b[i] = a[i] ** 2
  print(b)

vch(1, 10, 10)