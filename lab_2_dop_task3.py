a = float(input('Введите целое число: '))
c = 0
r = a 
i = 0
if a < 0:
  a = -1 * a
  r = a
  while r > 0:
    i += 1
    r = r // 10
  while a > 0:
    i = i - 1
    b = a % 10
    a = a // 10
    c = c + b  * (10 ** i)  
  c  = -1 * c
else:
  while r > 0:
    i += 1
    r = r // 10
  while a > 0:
    i = i - 1
    b = a % 10
    a = a // 10
    c = c + b  * (10 ** i)

print(c)