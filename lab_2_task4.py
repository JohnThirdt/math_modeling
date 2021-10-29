c = int(input('Введите натуральное число: '))
p = 1
v = 1
print(p, v, end=' ')
for i in range (0, c+1, 1):
  m = v + p
  print(m, end=' ')
  p = v
  v = m

print(' ')