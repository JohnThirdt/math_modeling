def srzn(*args):
  l = len(args)
  k = 0
  for i in range (l):
    k = k + args[i]
  print(k / l)

srzn(5, 6 , 10)