# Напишите программу, которая по заданному номеру четверти показывает диапазон возможных
# координат точек в этой четверти (x и y)

part = int(input())

if part == 1:
    print("x>0; y>0")
if part == 2:
    print("x<0; y>0")
if part == 3:
    print("x<0; y<0")
if part == 4:
    print("x>0; y<0")
