# Написать функцию вычисляющую площадь паралепипида, с ребрами а, б, с. функция должна содержать в себе др ф
# вычислюяющую площади прямоугольников.

# def s_parallel(a, b, c):
#     def pl_square(i, j):
#         return i * j
#
#     s = 2 * (pl_square(a, b) + pl_square(a, c) + pl_square(b, c))
#     return s
#
#
# print(s_parallel(2, 4, 6))
# print(s_parallel(5, 8, 2))
# print(s_parallel(1, 6, 8))


# С глобальной переменной
# s = 0
#
# def s_parallel(a, b, c):
#     def pl_square(i, j):
#         return i * j
#
#     global s
#     s = 2 * (pl_square(a, b) + pl_square(a, c) + pl_square(b, c))
#     return s
#
#
# print(s_parallel(2, 4, 6))
# print(s_parallel(5, 8, 2))
# print(s_parallel(1, 6, 8))

#С локальной переменной

def s_parallel(a, b, c):
    s = 0

    def pl_square(i, j):
        nonlocal s
        s += i * j

    pl_square(a, b)
    pl_square(a, c)
    pl_square(b, c)

    return 2 * s


print(s_parallel(2, 4, 6))
print(s_parallel(5, 8, 2))
print(s_parallel(1, 6, 8))