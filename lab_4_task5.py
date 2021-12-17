import math
d = input('Введите назавние фигуры: ')
def spc(a):
 if a == 'круг':
   z = float(input('Введите радиус круга: '))
   s = z * math.pi
 elif a == 'прямоугольник':
   z = float(input('Введите сторону первую: '))
   m = float(input('Введите сторону вторую: '))
   s = z * m 
 else:
   m = float(input('Введите сторону : '))
   h = float(input('Введите высоту к этой стороне: '))
   s = m * h * 0.5
 print(s)
 
spc(d)