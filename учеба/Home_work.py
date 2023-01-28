# print("У меня получилось?")
# print("У меня получилось?") # проверка


# Задание: Создать лямбда-выражение, которое возвращает произведение трех чисел.
# abc = (lambda a: lambda b: lambda c: a * b * c)(2)(5)(5)
# print(abc)


# Создать лямбд-выражения для нахождения площадей фигур
# import math
# Scircl = ((lambda i: math.pi * (i*i)))
# print("Площадь круга равна: ", Scircl(2))
#
# srec = ((lambda x: lambda z: x * z)(10)(13))
# print("Площадь прямоугольника равна: ", srec)
#
# strap = ((lambda a: lambda b: lambda c: 0.5 * (c * (a + b)))(7)(5)(3))
# print("площадь трапеции равна: ", strap)


# Задание: отсортировать список по имени студентов по итоговым оцекам в порядке убывания.
# students = [
#     {'name': 'Jennifer', 'final': 98},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolya', 'final': 95}
# ]
#
# nameSort = sorted(students, key=lambda item: item['name'])
# print("Сортировка по имени возрастание: ", nameSort)
# finalSort = sorted(students, key=lambda f: f['final'])
# print("Сортировка по оценке, возрастание: ", finalSort)
# print("*" * 30)
# nameSortRew = sorted(students, key=lambda item: item['name'], reverse=True)
# print("Сортировка по имени убывание: ", nameSortRew)
# finalSortRew = sorted(students, key=lambda f: f['final'], reverse=True)
# print("Сортировка по оценке, убывание: ", finalSortRew)


# Получить минимальную и максимальную оценку студентов.
# students = [
#     {'name': 'Jennifer', 'final': 98},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolya', 'final': 95},
#     {'name': 'Maria', 'final': 89},
#     {'name': 'Wasian', 'final': 75},
#     {'name': 'Gosha', 'final': 34}
# ]
# minFinal = min(students, key=lambda f: f['final'])
# print("Минимальная оценка: ", minFinal)
# maxFinal = max(students, key=lambda f: f['final'])
# print("Максимальная оценка:", maxFinal)



# Дан список чисел, исрользую лябдавыражение возведите в квадрат и в куб все элементы списка.
# z = [3, 5, 7, 3, 9, 5, 7, 2]
# y = {'one': lambda i: i**2, 'two': lambda i: i**3}
# w = []
# v = []
# for j in z:
#     w.append(y['one'](j))
# print("Список z возведенный в квадрат", w)
# for j in z:
#     v.append(y['two'](j))
# print("Список z возведенный в куб", v)

