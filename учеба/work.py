
# def decor (arcs1, arcs2):
#     def arcs_dec(fn):
#         def wrap(x, y):
#             print(arcs1, x, arcs2, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return arcs_dec

# lst = [3, 6, 8, 9, 1, 2]
# print(lst)
# print("*" * 20)
# print(list(map(lambda elem: elem * lst.index(elem) ** 3, lst)))


# t = ('abcd', 'abc', 'adefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)


# b = [66, 99, 88, 59, 60, 4, 81, 65]
# res = list(filter(lambda s: s > 60, b))
# print(res)

# a = [15, 37, 36, 26, 27, 35, 27, 20, 24, 3]
# res = list(filter(lambda x: 10 < x <= 20, a))
# print(res)

# a = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda x: x % 15 == 0, a))
# print(res)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)

# m = [x **2 for x in range(20) if x % 2]
# print(m)
#
# def hellou():
#     return 'Hellou, I am func "hellou"'
#
# def super_func(func):
#     print("Hellou, I am func 'super_func'")
#     print(func())
#
#
# super_func(hellou)


# def hellou():
#     return 'Hellou, I am func "hellou"'
#
# test = hellou
#
# print(test())


# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
# @my_decorator
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# func_test()

#
# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print('Вызов функции', count)
#
#     return wrap
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()


def args_decorator(fn):
    def wrap(arg1, arg2):
        print("данные ", arg1, arg2)
        fn(arg1, arg2)
    return wrap


@args_decorator
def print_ful_name(first, last):
    print("меня зовут: ", first, last)



print_ful_name("Алиса", "Селезнева")