# Задание. дан список целых чисел. Нужно найти минимальное среди простых, и максимальное среди составных чисел.
import random as r


baza = [r.randint(2, 50) for i in range(10)]
basa_prost = []
basa_no_prost = []
k = 0  # счетчик

for i in baza:
    k = 0
    for j in range(2, i):
        if i % j == 0:
            k += 1
    if k == 0:
        basa_prost.append(i)
    else:
        basa_no_prost.append(i)

print("Начальный рандомный список: ", baza)
print("простые: ", basa_prost)
print("составные: ", basa_no_prost)
print()
print("*" * 50)
print()
print("минимальное среди простых чисел: ", min(basa_prost))
print("максимальное среди составных чисел: ", max(basa_no_prost))












#
# m = [[r.randint(1, 10)] for i in range(10)] # рандомный список
# n = [2, 3, 4, 5, 6, 7, 8, 9, ]
# k = 0 # счетчик
#
# print(baza)
# mpr = [] # список с простыми числами
# mnp = [] # список с составными числами
# # i = 0
# # j = 2
# print(m, "случайный список")
# print(n, "список 10")
# for x in range(len(m)):
#
#     for i in range(10):
#         if (m[i] // 2 == 0):
#             mnp.append(x)








# print(mnp, "список с составными числами")
#
# print(m, "список с простыми числами")


