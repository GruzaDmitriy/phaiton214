# Задание 1 Дан словарь. изменить з\п Бреда
a = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500},
}

for x in a:
    print(a[x])
print()
a['emp3']['salary'] = 8500

print()
print(a['emp3'])




# Задание 2 задаем словарь со студентами. пользователь вводит количество студентов, имя студента и оценку.
# программа выводит средний балл и имена вышесреднего балла.

n = int(input("Введите колличество студентов: "))
balls = []

journal = {i: [input("Имя студента: "), int(input("Оценка: "))] for i in range(0, n)}
print()
print("*" * 50)
print()
for x in journal:
    print("Имя студента: ", journal[x][0], "  полученная оценка: ", journal[x][1])
    balls.append(journal[x][1])
print()
print("Средняя оценка по гр: ", sum(balls)/n)
print()

srballs = sum(balls)/n
print()

for x in journal:
    if journal[x][1] > srballs:
        print("Студент имеющий балл выше среднего: ", journal[x][0], " получивший оценку: ", journal[x][1])





