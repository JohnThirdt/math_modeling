a = int(input('Введите порог до которого будут найдены все совершенные числа, включительно: '))
for i in range (1, a, 1):
  l = i
  for n in range(1, i, 1):
    if i % n == 0:
      l = l - n
  if l == 0:
    print(i)