#Задание 1: даны два списка одиноковой длинны. Создать из них словарь, так, чтобф элементф одного стали ключами,
# а элементы второго значениями.

# a = [1, 2, 3, 4, 5]
# d = ["a", "b", "c", "d", "f"]
# z = dict(zip(a, d))
# print(z)


#Зад 2: Создать словарь значения в котором числа от 1 до 10, значения те же числа в кубе.

# b = [i for i in range(1, 11)]
# print(b)
# c = [i**3 for i in b]
# print(c)
# z = dict(zip(b, c))
# print(z)

# Или
# z = {i: i**3 for i in range(1, 11)}
# print(z)


# Зад 3: Используя два списка создать новый словарь с использованием генератора словарей.
# b = [i for i in range(1, 6)]
# print(b)
# c = [i for i in 'ABCDE']
# print(c)
# z = dict(zip(b, c))
# print(z)


#Зад 4: Создать функцию для нахождения минимального значения произвольного количества аргументов
# b = []
# def to_min(*a):
#     b = []
#     for i in a:
#         b.append(i)
#         b.sort()
#
#     return b[0]
# # print(b)
# print(to_min(10, 9))
# print(to_min(2, 3, 4))
# print(to_min(3, 5, 10, 6))


#Задание 5: создать функцию для нахлждения суммы элементов, таким образом, чтобы складывалос предыдущее значение
# с текущим значением произвольного аргумента.
b = 0
def to_sum(*a):
    b = 0
    for i in a:
        b += i
        print(b, end=" ")
    return b

to_sum(3, 9, 1)
print()
to_sum(2, 5, 4, 2)
print()
to_sum(3, 5, 10, 6, 3)


