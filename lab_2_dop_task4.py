a = int(input('Введите натуральное число: '))
z = 0
for i in range(a - 1, 1, -1):
  z = 0
  if a % i == 0:
    for m in range(i - 1, 1, -1):
      if i % m == 0:
        z += 1
    if z == 0:
      print(i, end = ' ')
print( )

      
        
    
