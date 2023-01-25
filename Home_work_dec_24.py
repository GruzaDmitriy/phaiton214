# Задание 1. задать фигуру, посчитать ее площадь. вывести результат.
# import math
# a, b, c, d = 0, 0, 0, 0  #стороны фигуры.
# z = 0 # выбранная фигура
# pi = math.pi
# sp = 0 # полупериметр треуг
# s = 0 # площадь треуг
# print("Возможные фигуры:\n 1 - прямоугольник\n 2 - треугольник\n 3 - круг ")
# z = int(input("Выберите фигуру: "))
#
# while z < 10:
#     if z > 3:
#         print("Выбрано неверное обозначение фигуры. повторите выбор")
#         z = int(input("Выберите фигуру: "))
#     if z == 1:
#         a = int(input("Введите длинну одной стороны: "))
#         b = int(input("Введите длинну второй стороны: "))
#         print("Площадь прямоугольника равна: ", a * b )
#         break
#     if z ==2:
#         a = int(input("Введите длинну одной стороны: "))
#         b = int(input("Введите длинну второй стороны: "))
#         c = int(input("Введите длинну третьей стороны: "))
#         sp = (a + b + c)/2
#         s = (sp * (sp - a)*(sp - b)*(sp - c)) ** 0.5
#         print("Площадь треугольника равна: ", s)
#         break
#     if z == 3:
#         d = int(input("Введите диаметр окружности: "))
#         c = 0.25 * d * pi * d
#         print("Площадь окружности равна: ", c)
#         break


# Задание 2 Вывести случайный двумерный список. и транспонировать его.
# import random as r
# import math
#
# print("*" * 20, "рандомная матрица", "*" * 20)
# w = int(input("введите ширину списка: "))
# h = int(input("введите высоту списка: "))
# i, j = 0, 0
# matrix = [[[r.randint(1, 9)] for x in range(w)] for y in range(h)]
# mtr = []
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()
# print("*" * 20, "транспонированная матрица", "*" * 20)
# for row in matrix:
#     for x in row:
#         print(x)
#     print()
# print("не смог я ее транспонировать.....")


# Задание 3. Даны случайный список 6*6 и одномерный список. четные строки двумерного заменить одномерным.
# import random as r
# matrix = [[[r.randint(1, 9)] for x in range(6)] for y in range(6)]
# m = [[r.randint(1, 9)] for z in range(6)]
#
# print("*" * 20, "Двумерный спискок", "*" * 20)
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
# print("*" * 20, "Одномерный спискок", "*" * 20)
# for z in m:
#     print(z, end=" ")
# print()
# print()
# print("*" * 20, "Двумерный с замененными строками", "*" * 20)
# for row in range(len(matrix)):
#     if row % 2 != 0:
#         print(matrix[row])
#     else:
#         print(m)


#Задание 4. Случайна матрица 6 * 6. поменять местами строки 1-2, 3-4, 5-6.
# import random as r
# matrix = [[[r.randint(1, 9)] for x in range(6)] for y in range(6)]
# i = 0
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
# print("*" * 20, "Двумерный с замененными строками", "*" * 20)
#
# matrix[0], matrix[1] = matrix[1], matrix[0]
# matrix[2], matrix[3] = matrix[3], matrix[2]
# matrix[4], matrix[5] = matrix[5], matrix[4]
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()










# черновик
from random import randint
# n1 = int(input("Размер первого спика: "))
# n2 = int(input("Размер второго спика: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("первый список", a)
# print("второй список", b)
#
# c = a + b
# print("новый  список", c)
#
# z = []
# for i in range(len(a)):
#     if a[i] not in z:
#         z.append(a[i])
# print("новый  список", z)
# for i in range(len(b)):
#     if b[i] not in z:
#         z.append(b[i])
# print("список а + б без повторов", z)
#
# d = []
# for i in range(len(a)):
#     if b[i] in a and b[i] not in d:
#         d.append(b[i])
# print("общие элементы", d)
#
# f = [min(a), max(a), min(b), max(b)]
#
# print("мин и макс элементы списков", f)

# a = [randint(0, 9) for i in range(10)]
# z = []
# i = 0
#
# while i < 10:
#     if a[i] not in z:
#         z.append(a[i])
#         i += 1
#     a = [randint(0, 9) for i in range(10)]
# print(z)


# for i in range(len(a)):
#     if a[i] not in z:
#         z.append(a[i])
#         i += 1










