import numpy as np 
k = [4, 5, 2]
a = np.array(k)
def per(m=[0, 0, 0]):
  b = m[0]
  z = len(k)
  for i in range(1, z):
    b = b * m[i]
  print(b)

per(a)