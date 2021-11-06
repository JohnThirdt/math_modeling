a = int(input('Введите целое число: '))
if a < 0:
  a = -1 * a
  for i in range (1, a + 1, 1):
    if a // i == 0:
      print(i)
else:
  for i in range(1, a + 1, 1):
     if a // i == 0:
        print(i)
        a = a / i
     else:
        a = a