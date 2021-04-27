"""
По введенным пользователем координатам двух точек вывести уравнение прямой вида
y = kx + b, проходящей через эти точки.
Блок-схема:
https://drive.google.com/file/d/196cVvF4b0n5777cC9WIL_8Hv_DhbyGdH/view?usp=sharing
"""

x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))
k = (y1 - y2) / (x1 - x2)
b = y1 - k * x1
print(f'Уравнение прямой: y = {k} * x + {b}')
