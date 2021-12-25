def fib(n):
  k = 0
  l = 1
  z = 0
  for i in range (n):
    k = z + l
    z = l
    l = k
  print(k)
fib(11)