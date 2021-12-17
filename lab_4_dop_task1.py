def stp(a, n):
  k = a
  for i in range (n - 1):
    a = a * k
  print(a)
stp(3, 4)